% HEO_PhaseTransition_Model_Final.m
% Final MATLAB port of the Python v2 mechanistic-discrimination model
% Date: 2026-09-18
%
% Parameters are phenomenological and non-unique.

clear; clc; close all;

samples = {'HEO','BM-HEO','Mg-HEO','BM-Mg-HEO'};
relaxAmp_mV = [160.91995,176.285705,109.471430,144.254610];
t63_min = [8.680667,11.571433,11.006100,12.994499];
excessPeak_mV = [70.768566,44.071071,15.905027,21.096806];

Apt_mV = [71.463983,44.231708,14.734005,20.621347];
mu_z = [0.780141,0.681771,0.828576,0.671573];
sigL = [0.186021,0.161836,0.251359,0.253707];
sigR = [0.086943,0.115611,0.052265,0.127058];
sigmaLnTau = [0.25,0.65,0.40,0.75];

pulse_s = 600.0;
restEnd_s = 3600.0;

%% D-only negative control
Aref = relaxAmp_mV(1);
tref = t63_min(1);
Drel_locus = logspace(-0.6,0.6,300);
A_locus = Aref./sqrt(Drel_locus);
t_locus = tref./Drel_locus;

bestD = zeros(1,4);
A_dpred = zeros(1,4);
t_dpred = zeros(1,4);
jointResidual = zeros(1,4);

for k = 1:4
    obj = @(logD) ((Aref/sqrt(exp(logD))-relaxAmp_mV(k))/Aref).^2 + ...
                  ((tref/exp(logD)-t63_min(k))/tref).^2;
    logDopt = fminbnd(obj,-3,3);
    bestD(k) = exp(logDopt);
    A_dpred(k) = Aref/sqrt(bestD(k));
    t_dpred(k) = tref/bestD(k);
    jointResidual(k) = sqrt(obj(logDopt));
end

D_from_amp = (Aref/relaxAmp_mV(3))^2;
t63_if_amp_matched = tref/D_from_amp;
D_from_t63 = tref/t63_min(3);
A_if_t63_matched = Aref/sqrt(D_from_t63);

fprintf('\n=== D-only Mg contradiction ===\n');
fprintf('Amplitude-matched D/D_HEO = %.3f -> predicted t63 = %.2f min\n',D_from_amp,t63_if_amp_matched);
fprintf('t63-matched D/D_HEO = %.3f -> predicted amplitude = %.1f mV\n',D_from_t63,A_if_t63_matched);

T_Donly = table(samples',bestD',relaxAmp_mV',A_dpred',t63_min',t_dpred',jointResidual', ...
    'VariableNames',{'Sample','Best_D_over_DHEO','ObservedAmp_mV','PredictedAmp_mV', ...
    'Observed_t63_min','Predicted_t63_min','NormalizedJointResidual'});
writetable(T_Donly,'HEO_MATLAB_Donly_fit.csv');

figure;
plot(t_locus,A_locus,'DisplayName','D-only locus'); hold on;
for k = 1:4
    scatter(t63_min(k),relaxAmp_mV(k),60,'filled','DisplayName',samples{k});
    text(t63_min(k),relaxAmp_mV(k),['  ' samples{k}]);
end
xlabel('t_{63} (min)'); ylabel('Median relaxation amplitude (mV)');
title('Single-diffusivity discriminator'); legend('Location','best'); box on;

%% State-distributed transition profile
z = linspace(0.40,0.90,500);
figure; hold on;
for k = 1:4
    plot(z,asymGauss(z,Apt_mV(k),mu_z(k),sigL(k),sigR(k)),'DisplayName',samples{k});
end
xlabel('Normalized first-lithiation capacity, z = Q/Q_{max}');
ylabel('Modeled transition polarization (mV)');
title('Distributed phase-transition surrogate'); legend('Location','best'); box on;

%% 600 s pulse + 3600 s rest
medianTau_s = zeros(1,4);
transitionScale_mV = zeros(1,4);
modeled_t63_min = zeros(1,4);
windowFactor = zeros(1,4);

for k = 1:4
    target_s = 60*t63_min(k);
    sig = sigmaLnTau(k);
    f = @(logTau) finiteT63(exp(logTau),sig,pulse_s,restEnd_s)-target_s;
    logTauMed = fzero(f,[log(10),log(10000)]);
    medianTau_s(k) = exp(logTauMed);
    modeled_t63_min(k) = finiteT63(medianTau_s(k),sig,pulse_s,restEnd_s)/60;

    k3 = pulseRestKernel(3,medianTau_s(k),sig,pulse_s);
    kEnd = pulseRestKernel(restEnd_s,medianTau_s(k),sig,pulse_s);
    windowFactor(k) = k3-kEnd;
    transitionScale_mV(k) = excessPeak_mV(k)/windowFactor(k);
end

T_v2 = table(samples',medianTau_s',sigmaLnTau',modeled_t63_min',t63_min', ...
    windowFactor',transitionScale_mV',excessPeak_mV', ...
    'VariableNames',{'Sample','MedianStructuralTau_s','SigmaLnTau','Modeled_t63_min', ...
    'Observed_t63_min','FiniteWindowFactor','TransitionScale_mV','ObservedExcessPeak_mV'});
writetable(T_v2,'HEO_MATLAB_v2_parameters.csv');

rest_t = logspace(log10(3),log10(restEnd_s),500);
figure; hold on;
for k = 1:4
    K = arrayfun(@(tt) pulseRestKernel(tt,medianTau_s(k),sigmaLnTau(k),pulse_s),rest_t);
    Kend = pulseRestKernel(restEnd_s,medianTau_s(k),sigmaLnTau(k),pulse_s);
    remaining = transitionScale_mV(k).*(K-Kend);
    semilogx(rest_t/60,remaining,'DisplayName',samples{k});
end
xlabel('Rest time after 600 s pulse (min)');
ylabel('Modeled remaining transition polarization (mV)');
title('Pulse/rest phase-transition model'); legend('Location','best'); box on;

fprintf('\n=== Interpretation guardrails ===\n');
fprintf('D-only is a negative control; strongest rejection occurs for Mg.\n');
fprintf('SigmaLnTau is not uniquely identified from t63.\n');
fprintf('TransitionScale is phenomenological, not a direct phase fraction.\n');

function y = asymGauss(z,A,mu,sigmaLeft,sigmaRight)
    sigma = sigmaRight*ones(size(z));
    sigma(z<mu) = sigmaLeft;
    y = A.*exp(-0.5.*((z-mu)./sigma).^2);
end

function tau = tauModes(tauMedian,sigmaLn,n)
    if nargin < 3, n = 501; end
    p = ((1:n)-0.5)./n;
    normalQuantile = sqrt(2).*erfinv(2.*p-1);
    tau = tauMedian.*exp(sigmaLn.*normalQuantile);
end

function K = pulseRestKernel(tRest,tauMedian,sigmaLn,pulse_s)
    tau = tauModes(tauMedian,sigmaLn,501);
    build = 1-exp(-pulse_s./tau);
    K = mean(build.*exp(-tRest./tau));
end

function t63 = finiteT63(tauMedian,sigmaLn,pulse_s,restEnd_s)
    t0 = 3.0;
    k0 = pulseRestKernel(t0,tauMedian,sigmaLn,pulse_s);
    kEnd = pulseRestKernel(restEnd_s,tauMedian,sigmaLn,pulse_s);
    fun = @(t) (k0-pulseRestKernel(t,tauMedian,sigmaLn,pulse_s))./(k0-kEnd)-0.632;
    t63 = fzero(fun,[t0,restEnd_s]);
end
