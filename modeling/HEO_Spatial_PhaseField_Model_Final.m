function HEO_Spatial_PhaseField_Model_Final()
% HEO_Spatial_PhaseField_Model_Final
% Frozen MATLAB port of the final Python spatial phase-field mechanism model.
% Date: 2026-09-18
%
% PURPOSE
%   Mechanism-sufficiency test for HEO / BM-HEO / Mg-HEO / BM-Mg-HEO.
%   This is NOT a unique parameter-identification model and is NOT an
%   absolute-voltage fit.
%
% GOVERNING FREE ENERGY (dimensionless)
%   f = c*ln(c) + (1-c)*ln(1-c)
%     + W*phi^2*(1-phi)^2
%     + K*(cstar-c)*phi
%     + Gmg*phi
%     + 0.5*Bel*qel(r)*phi^2
%     - Ssurf*wsurf(r)*phi
%     + 0.5*kappa*|grad(phi)|^2
%
%   qel(r)   = 1-exp(-(1-r)/ell_relief)
%   wsurf(r) = exp(-(1-r)/ell_wet)
%
%   mu = ln(c/(1-c)) - K*phi
%   dc/dt   = -div(J),  J = -Ddim*grad(mu)
%   dphi/dt = -Mphi*deltaG/deltaphi
%
% PROTOCOL
%   600 s pulse + 3600 s rest, 50 GITT states.
%   Refined dimensionless inward flux jin = 9e-6 gives Delta<c> ~ 0.0162
%   per pulse, comparable in order to the experimental normalized GITT step.
%
% IMPORTANT MODEL BOUNDARIES
%   - Bel is a reduced coherency-energy coordinate, not a full elasticity solve.
%   - Gaussian ensemble parameters are hypothesis-level coordinates.
%   - Absolute voltage and parameter uniqueness are not claimed.
%
% Authoritative development record:
%   modeling/HEO_MODELING_DEVELOPMENT_LOG_2026-09-18.md
%   modeling/HEO_FINAL_PYTHON_PHYSICS_GATE_2026-09-18.md

close all; clc;
cfg = base_config();

fprintf('Running HEO spatial phase-field model...\n');

p = material_params('HEO', cfg);
HEO = run_single_case(p, cfg);

p = material_params('Mg-HEO', cfg);
MG = run_single_case(p, cfg);

BM = run_gaussian_ensemble('BM-HEO', cfg);
BMMG = run_gaussian_ensemble('BM-Mg-HEO', cfg);

names = {'HEO','BM-HEO','Mg-HEO','BM-Mg-HEO'};
cases = {HEO,BM,MG,BMMG};

summaryVol = summarize_all(names, cases, 'vol');
summarySurf = summarize_all(names, cases, 'surf');

fprintf('\n=== Volume-averaged chemical-potential readout ===\n');
disp(summaryVol);
fprintf('\n=== Surface chemical-potential readout ===\n');
disp(summarySurf);

pythonTarget = table(...
    names', ...
    [1.00000; 0.23658; 0.13590; 0.18829], ...
    [0.06825; 0.08468; 0.03081; 0.04977], ...
    [22.02699; 26.91386; 40.17228; 40.17228], ...
    [1.00015; 1.00015; 0.21436; 0.82411], ...
    'VariableNames', {'Sample','PeakNorm_Python','MomentWidth_Python', ...
                      't63min_Python','FinalPhi_Python'});

fprintf('\n=== Frozen Python reference snapshot (directional target) ===\n');
disp(pythonTarget);

assert_directional_tests(summaryVol, 'volume-mu');
assert_directional_tests(summarySurf, 'surface-mu');

fprintf('\nAll directional unit tests PASSED.\n');
fprintf('Reminder: passing these tests does not imply parameter uniqueness.\n');

writetable(summaryVol,  'HEO_Spatial_PhaseField_MATLAB_Summary_VolumeMu.csv');
writetable(summarySurf, 'HEO_Spatial_PhaseField_MATLAB_Summary_SurfaceMu.csv');
make_summary_figure(summaryVol, summarySurf);
end

function cfg = base_config()
cfg.N = 18;
cfg.kappa = 0.002;
cfg.jin = 9e-6;
cfg.pulse_s = 600;
cfg.rest_s = 3600;
cfg.ncycles = 50;
cfg.nRestLog = 50;
cfg.nQuantiles = 11;
cfg.c0 = 0.10;
cfg.phi0 = 0.0;
cfg.odePulse = odeset('RelTol',1e-5,'AbsTol',5e-8,'MaxStep',60);
cfg.odeRest  = odeset('RelTol',1e-5,'AbsTol',5e-8,'MaxStep',100);
tLog = logspace(log10(0.2), log10(cfg.rest_s), cfg.nRestLog);
cfg.restTimes = unique([0, 3, tLog, cfg.rest_s]);
end

function p = material_params(name, cfg)
p.name = name;
p.N = cfg.N;
p.kappa = cfg.kappa;
p.jin = cfg.jin;
p.cstar = 0.60;

switch name
    case 'HEO'
        p.Ddim = 0.0015; p.Mphi = 0.015; p.W = 0.60; p.K = 1.80;
        p.Gmg = 0.00; p.Bel = 0.20; p.ell_relief = 0.08;
        p.Ssurf = 0.08; p.ell_wet = 0.06;
    case 'Mg-HEO'
        p.Ddim = 0.0015; p.Mphi = 0.0006; p.W = 0.80; p.K = 1.80;
        p.Gmg = 0.38; p.Bel = 0.20; p.ell_relief = 0.08;
        p.Ssurf = 0.08; p.ell_wet = 0.06;
    case 'BM-HEO'
        p.Ddim = 0.0030; p.Mphi = NaN; p.W = 0.50; p.K = 1.60;
        p.Gmg = 0.00; p.Bel = 0.25; p.ell_relief = 0.20;
        p.Ssurf = NaN; p.ell_wet = 0.12;
    case 'BM-Mg-HEO'
        p.Ddim = 0.0030; p.Mphi = NaN; p.W = 0.70; p.K = 1.70;
        p.Gmg = 0.30; p.Bel = 0.25; p.ell_relief = 0.20;
        p.Ssurf = NaN; p.ell_wet = 0.12;
    otherwise
        error('Unknown material name: %s', name);
end
end

function geom = make_geometry(p)
N = p.N;
geom.re = linspace(0,1,N+1)';
geom.rc = 0.5*(geom.re(1:end-1) + geom.re(2:end));
geom.A = geom.re.^2;
geom.V = (geom.re(2:end).^3 - geom.re(1:end-1).^3)/3;
d = 1 - geom.rc;
geom.qel = 1 - exp(-d/max(p.ell_relief,1e-12));
geom.wsurf = exp(-d/max(p.ell_wet,1e-12));
end

function out = run_single_case(p, cfg)
geom = make_geometry(p);
N = p.N;
y = [cfg.c0*ones(N,1); cfg.phi0*ones(N,1)];
nC = cfg.ncycles;
nR = numel(cfg.restTimes);

Vvol = zeros(nC,nR);
Vsurf = zeros(nC,nR);
cbar = zeros(nC,1);
phibar = zeros(nC,1);

for k = 1:nC
    [~,Yp] = ode15s(@(t,yy) rhs_pf(t,yy,p,geom,true), ...
                    [0 cfg.pulse_s], y, cfg.odePulse);
    yp = Yp(end,:)';

    [~,Yr] = ode15s(@(t,yy) rhs_pf(t,yy,p,geom,false), ...
                    cfg.restTimes, yp, cfg.odeRest);

    for j = 1:nR
        [Vvol(k,j),Vsurf(k,j),~,~] = observables(Yr(j,:)',p,geom);
    end

    y = Yr(end,:)';
    [~,~,cbar(k),phibar(k)] = observables(y,p,geom);
end

out.name = p.name;
out.Vvol = Vvol;
out.Vsurf = Vsurf;
out.cbar = cbar;
out.phibar = phibar;
out.restTimes = cfg.restTimes(:)';
out = add_relaxation_descriptors(out);
end

function out = run_gaussian_ensemble(name, cfg)
base = material_params(name,cfg);
nQ = cfg.nQuantiles;
prob = ((1:nQ)-0.5)/nQ;
x = sqrt(2)*erfinv(2*prob-1);
weights = ones(1,nQ)/nQ;

members = cell(1,nQ);
for q = 1:nQ
    p = base;
    if strcmp(name,'BM-HEO')
        p.Ssurf = 0.15 + 0.06*x(q);
        p.Mphi  = 0.008*exp(-0.6*x(q));
    elseif strcmp(name,'BM-Mg-HEO')
        p.Ssurf = 0.22 + 0.075*x(q);
        p.Mphi  = 0.0008*exp(-0.6*x(q));
    else
        error('Ensemble requested for non-BM case.');
    end
    p.name = sprintf('%s_q%02d',name,q);
    members{q} = run_single_case(p,cfg);
end

Vvol = 0; Vsurf = 0; cbar = 0; phibar = 0;
for q = 1:nQ
    Vvol = Vvol + weights(q)*members{q}.Vvol;
    Vsurf = Vsurf + weights(q)*members{q}.Vsurf;
    cbar = cbar + weights(q)*members{q}.cbar;
    phibar = phibar + weights(q)*members{q}.phibar;
end

out.name = name;
out.Vvol = Vvol;
out.Vsurf = Vsurf;
out.cbar = cbar;
out.phibar = phibar;
out.restTimes = members{1}.restTimes;
out.quantile_x = x;
out.quantile_weights = weights;
out = add_relaxation_descriptors(out);
end

function dy = rhs_pf(~,y,p,geom,pulseOn)
N = p.N;
c = y(1:N);
phi = y(N+1:2*N);
cc = min(max(c,1e-6),1-1e-6);
mu = log(cc./(1-cc)) - p.K*phi;

J = zeros(N+1,1);
drc = geom.rc(2:end) - geom.rc(1:end-1);
J(2:N) = -p.Ddim*(mu(2:end)-mu(1:end-1))./drc;
J(1) = 0;
if pulseOn
    J(end) = -p.jin;
else
    J(end) = 0;
end
dc = -(geom.A(2:end).*J(2:end) - geom.A(1:end-1).*J(1:end-1))./geom.V;

gradPhi = zeros(N+1,1);
gradPhi(2:N) = (phi(2:end)-phi(1:end-1))./drc;
gradPhi(1) = 0;
gradPhi(end) = 0;
lapPhi = (geom.A(2:end).*gradPhi(2:end) - ...
          geom.A(1:end-1).*gradPhi(1:end-1))./geom.V;

gprime = 2*phi.*(1-phi).*(1-2*phi);
dGdphi = p.W*gprime ...
        + p.K*(p.cstar-c) ...
        + p.Gmg ...
        + p.Bel*geom.qel.*phi ...
        - p.Ssurf*geom.wsurf ...
        - p.kappa*lapPhi;

dphi = -p.Mphi*dGdphi;
dphi(phi<=0 & dphi<0) = 0;
dphi(phi>=1 & dphi>0) = 0;

dy = [dc; dphi];
end

function [Vvol,Vsurf,cbar,phibar] = observables(y,p,geom)
N = p.N;
c = y(1:N);
phi = y(N+1:2*N);
cc = min(max(c,1e-6),1-1e-6);
mu = log(cc./(1-cc)) - p.K*phi;
Vvol = -sum(mu.*geom.V)/sum(geom.V);
Vsurf = -mu(end);
cbar = sum(c.*geom.V)/sum(geom.V);
phibar = sum(phi.*geom.V)/sum(geom.V);
end

function out = add_relaxation_descriptors(out)
out.ampVol = zeros(size(out.cbar));
out.ampSurf = zeros(size(out.cbar));
out.t63Vol_s = NaN(size(out.cbar));
out.t63Surf_s = NaN(size(out.cbar));

for k = 1:numel(out.cbar)
    [out.ampVol(k),out.t63Vol_s(k)] = one_relaxation(out.restTimes,out.Vvol(k,:));
    [out.ampSurf(k),out.t63Surf_s(k)] = one_relaxation(out.restTimes,out.Vsurf(k,:));
end
end

function [amp,t63] = one_relaxation(t,V)
[~,i3] = min(abs(t-3));
amp = abs(V(end)-V(i3));
if amp <= 1e-12
    t63 = NaN;
    return;
end
F = abs((V-V(i3))/(V(end)-V(i3)));
idx = find(t>=3 & F>=0.632,1,'first');
if isempty(idx)
    t63 = NaN;
else
    t63 = t(idx)-3;
end
end

function T = summarize_all(names,cases,mode)
n = numel(names);
Peak = zeros(n,1);
MomentWidth = zeros(n,1);
t63min = zeros(n,1);
cPeak = zeros(n,1);
FinalPhi = zeros(n,1);

for i = 1:n
    C = cases{i};
    if strcmp(mode,'vol')
        amp = C.ampVol;
        tau = C.t63Vol_s;
    else
        amp = C.ampSurf;
        tau = C.t63Surf_s;
    end

    [Peak(i),im] = max(amp);
    cPeak(i) = C.cbar(im);
    t63min(i) = tau(im)/60;
    FinalPhi(i) = C.phibar(end);

    w = amp/sum(amp);
    center = sum(w.*C.cbar);
    MomentWidth(i) = sqrt(sum(w.*(C.cbar-center).^2));
end

PeakNorm = Peak/Peak(1);
T = table(names',Peak,PeakNorm,MomentWidth,t63min,cPeak,FinalPhi, ...
    'VariableNames',{'Sample','Peak','PeakNormToHEO','MomentWidth_c', ...
                     't63Peak_min','cPeak','FinalPhi'});
end

function assert_directional_tests(T,label)
S = containers.Map(T.Sample,1:height(T));
iH = S('HEO');
iB = S('BM-HEO');
iM = S('Mg-HEO');
iBM = S('BM-Mg-HEO');

checks = [ ...
    T.Peak(iB) < T.Peak(iH), ...
    T.MomentWidth_c(iB) > T.MomentWidth_c(iH), ...
    T.t63Peak_min(iB) > T.t63Peak_min(iH), ...
    T.Peak(iM) < T.Peak(iH), ...
    T.t63Peak_min(iM) > T.t63Peak_min(iH), ...
    T.FinalPhi(iM) < T.FinalPhi(iH), ...
    T.Peak(iBM) > T.Peak(iM), ...
    T.Peak(iBM) < T.Peak(iH), ...
    T.FinalPhi(iBM) > T.FinalPhi(iM), ...
    T.FinalPhi(iBM) < T.FinalPhi(iH)];

labels = { ...
    'BM peak < HEO', ...
    'BM width > HEO', ...
    'BM t63 > HEO', ...
    'Mg peak < HEO', ...
    'Mg t63 > HEO', ...
    'Mg phi < HEO', ...
    'BM-Mg peak > Mg', ...
    'BM-Mg peak < HEO', ...
    'BM-Mg phi > Mg', ...
    'BM-Mg phi < HEO'};

fprintf('\nDirectional tests (%s):\n',label);
for k = 1:numel(checks)
    fprintf('  %-24s : %s\n',labels{k},string(checks(k)));
end
assert(all(checks), 'Directional test failed for %s readout.', label);
end

function make_summary_figure(Tv,Ts)
n = height(Tv);
x = 1:n;
figure('Color','w','Position',[100 100 1100 800]);

subplot(2,2,1);
bar(x,[Tv.PeakNormToHEO Ts.PeakNormToHEO]);
set(gca,'XTick',x,'XTickLabel',Tv.Sample,'XTickLabelRotation',15);
ylabel('Peak relaxation / HEO');
title('Transition-associated peak');
legend({'volume-\mu','surface-\mu'},'Location','best'); box off;

subplot(2,2,2);
bar(x,[Tv.t63Peak_min Ts.t63Peak_min]);
set(gca,'XTick',x,'XTickLabel',Tv.Sample,'XTickLabelRotation',15);
ylabel('t_{63} at peak (min)');
title('Structural relaxation time');
legend({'volume-\mu','surface-\mu'},'Location','best'); box off;

subplot(2,2,3);
bar(x,[Tv.MomentWidth_c Ts.MomentWidth_c]);
set(gca,'XTick',x,'XTickLabel',Tv.Sample,'XTickLabelRotation',15);
ylabel('Moment width in mean c');
title('State-distribution width');
legend({'volume-\mu','surface-\mu'},'Location','best'); box off;

subplot(2,2,4);
bar(x,Tv.FinalPhi);
set(gca,'XTick',x,'XTickLabel',Tv.Sample,'XTickLabelRotation',15);
ylabel('Final transformed-fraction proxy');
ylim([0 1.08]);
title('Mg suppression and BM-Mg partial recovery'); box off;

try
    exportgraphics(gcf,'HEO_Spatial_PhaseField_MATLAB_Final.png','Resolution',300);
catch
    saveas(gcf,'HEO_Spatial_PhaseField_MATLAB_Final.png');
end
end
