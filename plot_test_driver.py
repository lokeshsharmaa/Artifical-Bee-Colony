from src.functions.rastriginfn import RastriginFn


def plots_gen(fn, img_name, points):
    # fn.graph_fn()
    fn.contour_plot(img_name, points)


plots_gen(RastriginFn(2), 'rastrigin.png', [(0, 0), (1, 1), (2, 1)])
# plots_gen(easom_fn(), 'easom.png', [(0, 0), (1, 1), (2, 1), (math.pi, math.pi)])
# plots_gen(sphere_fn(2), 'sphere.png', [(0, 0), (1, 1), (2, 1)])
# plots_gen(himmelbau_fn(), 'himmelbau.png',
#           [(0, 0), (3.0, 2.0), (-2.805118, 3.131312), (-3.779310, -3.283186), (3.584428, -1.848126)])
