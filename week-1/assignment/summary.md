
## Part 2 
## Phase 2: Heatmap Analysis

Correlation values range from -1 to 1.

- Positive values mean both features increase together.
- Negative values mean one feature increases while the other decreases.
- Values near 0 mean weak relation.

From the heatmap:

- Total_Words and Total_Characters have very high correlation (0.99), so they contain almost the same information.
- x_05 and x_02 have strong positive correlation (0.78).
- x_25 and x_100 have strong positive correlation (0.74).
- x_54 and x_74 have strong negative correlation (-0.79).

This shows the presence of multicollinearity, where multiple features carry similar information.

Multicollinearity can create redundancy because highly related features provide similar patterns. This can make some models less stable and increase unnecessary complexity.

## Phase 3: t-SNE and UMAP Analysis

UMAP produced a more compact and visually organized representation of the data. Since UMAP is designed to preserve larger relationships in the data, it may preserve the overall structure better than t-SNE.

Late and on-time submissions do not form clearly separated clusters. Both classes appear mixed within the same regions, which suggests that the features do not naturally separate the two classes.

Comparing all features with the top 15 features, the top 15 feature plots show slightly more compact local grouping, but the overall clustering pattern remains similar. This suggests that reducing the number of features had only a small effect on the data structure.
