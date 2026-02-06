import imageio.v3 as iio 

filenames = [ 'headshot1.png', 'headshot2.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('headshots.gif', images, duration = 500, loop = 0)
