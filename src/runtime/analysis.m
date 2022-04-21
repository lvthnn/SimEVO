%% Read in data
cd('~/Github/SimEVO/src/runtime/');
data = readmatrix('data.csv');

%% Dimension variables
max_load = data(:,1);
n = data(:,2);
C = data(:,3);

%% Create plot
tri = delaunay(n, C);
S = trisurf(tri, n, C, max_load);
S.EdgeAlpha = 0.3;

hold on;
colormap("summer");