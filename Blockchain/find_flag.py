import hashlib
import os
import copy

def calculate_block(b_dir):
    base, cur_dir = b_dir.split('\\')
    splitted_dir = cur_dir.split('-')
    height = int(splitted_dir[1][-1:])
    sons = int(splitted_dir[2][-1:])
    mt_hashes = []

    files_only_num = []
    for filename in os.listdir(b_dir):
        filename = filename.split('_')
        files_only_num.append(int(filename[1]))

    files_only_num.sort()
    filenames = []
    for filename in files_only_num:
        filenames.append('tx_{0}'.format(filename))

    # save leafs
    # for filename in os.listdir(b_dir):
    for filename in filenames:
        # print filename
        file_content = open(b_dir + '\\' + filename, 'r').read()
        first_hash, second_hash, num = file_content.split('\t')
        # tx_hash = hashlib.md5(first_hash+second_hash).hexdigest()
        # tx_hash = hashlib.md5(num).hexdigest()
        tx_hash = hashlib.md5(file_content).hexdigest()
        # tx_hash = hashlib.md5(first_hash + second_hash + hashlib.md5(num).hexdigest()).hexdigest()
        mt_hashes.append(tx_hash)

    # now calculate the block root
    tmp_mt_hashes = []
    start_index = 0
    while height > 0:
        while start_index < len(mt_hashes):
            tx_hash = ''
            for i in range(sons):
                tx_hash += mt_hashes[start_index + i]
            tx_hash = hashlib.md5(tx_hash).hexdigest()
            tmp_mt_hashes.append(tx_hash)
            start_index += sons
        mt_hashes = copy.deepcopy(tmp_mt_hashes)
        tmp_mt_hashes = []
        start_index = 0
        height -= 1
    return mt_hashes[0]

current_hash = 'a861f335d4d457a7c1d00640da380dc4'
for block_dir in os.listdir('blocks'):
    calculated_hash = calculate_block('blocks\\' + block_dir)
    current_hash = hashlib.md5(current_hash + calculated_hash).hexdigest()

pass