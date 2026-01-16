import imageio.v2 as imageio

filenames = [
    r'C:\\Users\\joshu\\OneDrive\\Desktop\\python\\Codex\\team-pic1.png', 
    r'C:\\Users\\joshu\\OneDrive\\Desktop\\python\\Codex\\team-pic2.png'
]
images = [imageio.imread(fn) for fn in filenames]

imageio.mimsave('team.gif', images, duration = .5, loop = 0)







