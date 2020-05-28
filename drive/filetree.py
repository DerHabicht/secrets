import os


def list_files(root):
    tree = ''

    for r, dirs, files in os.walk(root):
        level = r.replace(root, '').count(os.sep)
        indent = ' ' * 4 * level
        tree += '{}{}/'.format(indent, os.path.basename(r)) + '\n'
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            tree += '{}{}'.format(subindent, f) + '\n'

    return tree


def build_tree(root):
    tree = {'.': []}

    for f in os.listdir(root):
        if os.path.isdir(os.path.join(root, f)):
            tree[f] = build_tree(os.path.join(root, f))
        else:
            tree['.'].append(f)

    return tree
