import matplotlib.pyplot as plt
import pandas as pd

# get file
iris = pd.read_csv('iris.csv')


# initialize figure parameters
colors = ['r', 'y', 'b']
species = iris.Species.unique()
plt.figure(figsize=(10, 10))


# sub figures
# figure 1
plt.subplot(4, 4, 13)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Petal.Width'],
                iris.loc[iris.Species == species[i], 'Petal.Width'],
                s=5, c=colors[i], label=species[i])
plt.title("Petal.Width vs Petal.Width")
plt.xlabel('Petal.Width')
plt.ylabel('Petal.Width')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 2
plt.subplot(4, 4, 14)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Petal.Width'],
                iris.loc[iris.Species == species[i], 'Petal.Length'],
                s=5, c=colors[i], label=species[i])
plt.title("Petal.Width vs Petal.Length")
plt.xlabel('Petal.Width')
plt.ylabel('Petal.Length')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 3
plt.subplot(4, 4, 15)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Petal.Width'],
                iris.loc[iris.Species == species[i], 'Sepal.Width'],
                s=5, c=colors[i], label=species[i])
plt.title("Petal.Width vs Sepal.Width")
plt.xlabel('Petal.Width')
plt.ylabel('Sepal.Width')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 4
plt.subplot(4, 4, 16)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Petal.Width'],
                iris.loc[iris.Species == species[i], 'Sepal.Length'],
                s=5, c=colors[i], label=species[i])
plt.title("Petal.Width vs Sepal.Length")
plt.xlabel('Petal.Width')
plt.ylabel('Sepal.Length')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 5
plt.subplot(4, 4, 9)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Petal.Length'],
                iris.loc[iris.Species == species[i], 'Petal.Width'],
                s=5, c=colors[i], label=species[i])
plt.title("Petal.Length vs Petal.Width")
plt.xlabel('Petal.Length')
plt.ylabel('Petal.Width')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 6
plt.subplot(4, 4, 10)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Petal.Length'],
                iris.loc[iris.Species == species[i], 'Petal.Length'],
                s=5, c=colors[i], label=species[i])
plt.title("Petal.Length vs Petal.Length")
plt.xlabel('Petal.Length')
plt.ylabel('Petal.Length')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 7
plt.subplot(4, 4, 11)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Petal.Length'],
                iris.loc[iris.Species == species[i], 'Sepal.Width'],
                s=5, c=colors[i], label=species[i])
plt.title("Petal.Length vs Sepal.Width")
plt.xlabel('Petal.Length')
plt.ylabel('Sepal.Width')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 8
plt.subplot(4, 4, 12)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Petal.Length'],
                iris.loc[iris.Species == species[i], 'Sepal.Length'],
                s=5, c=colors[i], label=species[i])
plt.title("Petal.Length vs Sepal.Length")
plt.xlabel('Petal.Length')
plt.ylabel('Sepal.Length')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 9
plt.subplot(4, 4, 5)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Sepal.Width'],
                iris.loc[iris.Species == species[i], 'Petal.Width'],
                s=5, c=colors[i], label=species[i])
plt.title("Sepal.Width vs Petal.Width")
plt.xlabel('Sepal.Width')
plt.ylabel('Petal.Width')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 10
plt.subplot(4, 4, 6)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Sepal.Width'],
                iris.loc[iris.Species == species[i], 'Petal.Length'],
                s=5, c=colors[i], label=species[i])
plt.title("Sepal.Width vs Petal.Length")
plt.xlabel('Sepal.Width')
plt.ylabel('Petal.Length')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 11
plt.subplot(4, 4, 7)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Sepal.Width'],
                iris.loc[iris.Species == species[i], 'Sepal.Width'],
                s=5, c=colors[i], label=species[i])
plt.title("Sepal.Width vs Sepal.Width")
plt.xlabel('Sepal.Width')
plt.ylabel('Sepal.Width')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 12
plt.subplot(4, 4, 8)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Sepal.Width'],
                iris.loc[iris.Species == species[i], 'Sepal.Length'],
                s=5, c=colors[i], label=species[i])
plt.title("Sepal.Width vs Sepal.Length")
plt.xlabel('Sepal.Width')
plt.ylabel('Sepal.Length')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 13
plt.subplot(4, 4, 1)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Sepal.Length'],
                iris.loc[iris.Species == species[i], 'Petal.Width'],
                s=5, c=colors[i], label=species[i])
plt.title("Sepal.Length vs Petal.Width")
plt.xlabel('Sepal.Length')
plt.ylabel('Petal.Width')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 14
plt.subplot(4, 4, 2)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Sepal.Length'],
                iris.loc[iris.Species == species[i], 'Petal.Length'],
                s=5, c=colors[i], label=species[i])
plt.title("Sepal.Length vs Petal.Length")
plt.xlabel('Sepal.Length')
plt.ylabel('Petal.Length')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 15
plt.subplot(4, 4, 3)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Sepal.Length'],
                iris.loc[iris.Species == species[i], 'Sepal.Width'],
                s=5, c=colors[i], label=species[i])
plt.title("Sepal.Length vs Sepal.Width")
plt.xlabel('Sepal.Length')
plt.ylabel('Sepal.Width')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)

# figure 16
plt.subplot(4, 4, 4)
for i in range(len(species)):
    plt.scatter(iris.loc[iris.Species == species[i], 'Sepal.Length'],
                iris.loc[iris.Species == species[i], 'Sepal.Length'],
                s=5, c=colors[i], label=species[i])
plt.title("Sepal.Length vs Sepal.Length")
plt.xlabel('Sepal.Length')
plt.ylabel('Sepal.Length')
plt.grid(True, linestyle='--', alpha=0.8)
plt.legend(loc='upper right', fontsize=5)


# draw figures
plt.tight_layout(pad=1.08)
plt.show()
