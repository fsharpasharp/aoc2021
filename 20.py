from itertools import product

with open('input', 'r') as f:
    output, input_image = f.read().split('\n\n')
input_image = input_image.split()

grid_area = 9
def build_mapping(mapping, values, key=""):
    if len(key) == grid_area:
        mapping[key] = values.pop()
        return
    build_mapping(mapping, values, key+".")
    build_mapping(mapping, values, key+"#")

def add_padding(image, c='.'):
    for i in range(len(image)):
        image[i] = c + image[i] + c
    padding = ''.join([c]*len(image[0]))
    image.insert(0, padding)
    image.append(padding)

def remove_padding(image):
    for i in range(len(image)):
        image[i] = image[i][1:len(image)-1]
    image.pop(0)
    image.pop()

def ranges(image):
    return product(range(1,len(image)-1), range(1, len(image[0])-1))

def update(image, mapping):
    def adjacent(y, x):
        s = ""
        for i in range(-1,2):
            s += image[y+i][x-1:x+2]
        return s
    new_image = [[] for i in range(len(image))]
    for i, x in enumerate(image):
        new_image[i] = list(x)
    for i, j in ranges(new_image):
        new_image[i][j] = mapping[adjacent(i,j)]
    for i, x in enumerate(new_image):
        new_image[i] = ''.join(x)

    return new_image

mapping = dict()
build_mapping(mapping, list(reversed(output)))

for i in range(2):
    add_padding(input_image, '.')
for i in range(50):
    input_image = update(input_image, mapping)
    remove_padding(input_image)
    for j in range(2):
        if i%2 == 1:
            add_padding(input_image, '.')
        else:
            add_padding(input_image, '#')
print(''.join(input_image).count('#'))
