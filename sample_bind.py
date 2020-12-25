#采样并把正负样本结合
#需要修改文件名
"""------------------------------"""
#采样正样本
promoters = open('GM/initial/GM_promoter_pos1.fasta')
enhancers = open('GM/initial/GM_enhencer_pos1.fasta')


pro_array = promoters.read().split('\n')[:-1]
enh_array = enhancers.read().split('\n')[:-1]
print('data_length:', len(pro_array), len(enh_array))


labels = open('GM/initial/GMlabels_pos.txt')
l_array = labels.read().replace('\n', '')
print("labels:", len(l_array))

import random as r
size = 1000
sample = sorted([x * 2 for x in r.sample(range(len(pro_array) // 2), k=size)])
# %%
with open('GM/sample_feacture/sample_pos_promoters_1000.fasta', 'w') as p:
    with open('GM/sample_feacture/sample_pos_enhancers_1000.fasta', 'w') as e:
        with open('GM/sample_feacture/sample_pos_labels_1000.txt', 'w') as l:
                for index in sample:


                    #====== 写入分开的文件 =======
                    p.write(pro_array[index])
                    p.write('|')
                    p.write(l_array[index // 2])
                    p.write('|')
                    p.write('training')
                    p.write('\n')
                    p.write(pro_array[index + 1])
                    p.write('\n')

                    e.write(enh_array[index])
                    e.write('|')
                    e.write(l_array[index // 2])
                    e.write('|')
                    e.write('training')
                    e.write('\n')
                    e.write(enh_array[index + 1])
                    e.write('\n')

                    l.write(l_array[index // 2])
                    l.write('\n')
promoters.close()
enhancers.close()
# %%

"""----------------------------------"""
#负样本采样
promoters = open('GM/initial/GM_promoter_neg1.fasta')
enhancers = open('GM/initial/GM_enhencer_neg1.fasta')


pro_array = promoters.read().split('\n')[:-1]
enh_array = enhancers.read().split('\n')[:-1]
print('data_length:', len(pro_array), len(enh_array))


labels = open('GM/initial/GMlabels_neg.txt')
l_array = labels.read().replace('\n', '')
print("labels:", len(l_array))

import random as r
size = 3000
sample = sorted([x * 2 for x in r.sample(range(len(pro_array) // 2), k=size)])
# %%
with open('GM/sample_feacture/sample_neg_promoters_3000.fasta', 'w') as p:
    with open('GM/sample_feacture/sample_neg_enhancers_3000.fasta', 'w') as e:
        with open('GM/sample_feacture/sample_neg_labels_3000.txt', 'w') as l:
                for index in sample:


                    #====== 写入分开的文件 =======
                    p.write(pro_array[index])
                    p.write('|')
                    p.write(l_array[index // 2])
                    p.write('|')
                    p.write('training')
                    p.write('\n')
                    p.write(pro_array[index + 1])
                    p.write('\n')

                    e.write(enh_array[index])
                    e.write('|')
                    e.write(l_array[index // 2])
                    e.write('|')
                    e.write('training')
                    e.write('\n')
                    e.write(enh_array[index + 1])
                    e.write('\n')

                    l.write(l_array[index // 2])
                    l.write('\n')
promoters.close()
enhancers.close()

""""--------------------------------------"""
#合并正负样本

promoters = open('GM/sample_feacture/sample_pos_promoters_1000.fasta')
enhancers = open('GM/sample_feacture/sample_neg_promoters_3000.fasta')
pro_array = promoters.readlines()
enh_array = enhancers.readlines()
print('data_length:', len(pro_array), len(enh_array))
with open('GM/sample_feacture/GM_promoters_sample.fasta', 'w') as p:
    p.writelines(pro_array)
    p.writelines(enh_array)

promoters.close()
enhancers.close()



promoters = open('GM/sample_feacture/sample_pos_enhancers_1000.fasta')
enhancers = open('GM/sample_feacture/sample_neg_enhancers_3000.fasta')
pro_array = promoters.readlines()
enh_array = enhancers.readlines()
print('data_length:', len(pro_array), len(enh_array))
with open('GM/sample_feacture/GM_enhancers_sample.fasta', 'w') as p:
    p.writelines(pro_array)
    p.writelines(enh_array)

promoters.close()
enhancers.close()


