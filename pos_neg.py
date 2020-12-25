#分为正负样本
"""------------------------------"""
#需要修改文件名
promoters = open('NHEK/initial/NHEK_promoters.fasta')
enhancers = open('NHEK/initial/NHEK_enhancers.fasta')


pro_array = promoters.read().split('\n')[:-1]
enh_array = enhancers.read().split('\n')[:-1]
print('data_length:', len(pro_array), len(enh_array))


labels = open('NHEK/initial/NHEKlabels.txt')
l_array = labels.read().replace('\n', '')
print("labels:", len(l_array))

"""----------------------------------"""
#将启动子分为正负样本
with open('NHEK/initial/NHEK_promoter_pos1.fasta', 'w') as p:
    with open('NHEK/initial/NHEK_promoter_neg1.fasta', 'w') as e:
        with open('NHEK/initial/NHEKlabels_pos1.fasta', 'w') as l:
            for index in range(0, len(pro_array), 2):
                    #====== 写入分开的文件 =======

                    if l_array[index//2] =='1':
                        p.write(pro_array[index])
                        p.write('\n')
                        p.write(pro_array[index+1])
                        p.write('\n')
                        l.write(l_array[index//2])
                        l.write('\n')
                    elif l_array[index//2] =='0':
                        e.write(pro_array[index])
                        e.write('\n')
                        e.write(pro_array[index+1])
                        e.write('\n')

"""----------------------------------"""
#将增强子分为正负样本
with open('NHEK/initial/NHEK_enhencer_pos1.fasta', 'w') as p:
    with open('NHEK/initial/NHEK_enhencer_neg1.fasta', 'w') as e:
        with open('NHEK/initial/NHEKlabels_neg1.fasta', 'w') as l:
             for index in range(0,len(enh_array),2):
                    #====== 写入分开的文件 =======
                    if l_array[index//2] =='1':
                        p.write(enh_array[index])
                        p.write('\n')
                        p.write(enh_array[index+1])
                        p.write('\n')
                    elif l_array[index//2] =='0':
                        e.write(enh_array[index])
                        e.write('\n')
                        l.write(l_array[index // 2])
                        l.write('\n')
                        e.write(enh_array[index+1])
                        e.write('\n')

promoters.close()
enhancers.close()
# %%


