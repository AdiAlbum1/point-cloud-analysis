import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt
import random

# parameters:
# N: Number of points on generated plane
# M: number of noise points
N = 1000
M = 20

# ax + by + cz = d
def determine_plane_parameters():
    # randomly choose a, b, and d
    a = random.uniform(-3, 3)
    b = random.uniform(-3, 3)
    c = 1
    d = random.uniform(-3, 3)

    return a,b,c,d

def randomly_generate_plane_points(a, b, c, d, amount):
    plane_points = np.zeros((amount, 3))

    for i in range(N):
        x = random.uniform(-3,3)
        y = random.uniform(-3,3)
        z = d/c - (a/c)*x - (b/c)*y

        plane_points[i] = x,y,z

    return plane_points

def visualize_plane(plane_points, n_plane_points):
    xs, ys, zs = np.split(plane_points, 3, axis=1)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(xs[:n_plane_points], ys[:n_plane_points], zs[:n_plane_points], c='r')
    ax.scatter(xs[n_plane_points:], ys[n_plane_points:], zs[n_plane_points:], c='b')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

def add_noise_to_plane(plane_points):
    epsilon = 0.5
    noisy_plane_points = np.zeros(plane_points.shape)
    for i in range(len(noisy_plane_points)):
        noisy_plane_points[i] = plane_points[i] + np.random.normal(loc=0, scale=epsilon, size=3)

    return noisy_plane_points

def generate_noisy_points(amount):
    noise = np.random.uniform(low=-10, high=10, size=(amount, 3))
    return noise

if __name__ == "__main__":
    a, b, c, d = determine_plane_parameters()
    plane_points = randomly_generate_plane_points(a, b, c, d, N)

    # visualize_plane(plane_points)

    noisy_plane_points = add_noise_to_plane(plane_points)

    # visualize_plane(noisy_plane_points)

    noise = generate_noisy_points(M)

    all_points = np.vstack([noisy_plane_points, noise])
    visualize_plane(all_points, N)

    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(all_points)

    l = o3d.geometry.PointCloud.segment_plane(pcd, 0.01, 10, 10)
    print(l[0])
    print(a, b, c, d)