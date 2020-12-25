#合并提取到的特征并且合并启动子增强子
#需要修改文件名
#需要修改index范围(对应行数)

"""--------------------------------------"""
#合并增强子Kmer,NAC提取的特征
promoters = open('NHEK/sample_feacture/NHEK_enhencers_Kmer.weka')
enhancers = open('NHEK/sample_feacture/NHEK_enhencers_NAC.weka')
pro_array = promoters.read().split('\n')[:-1]
enh_array = enhancers.read().split('\n')[:-1]
print('data_length:',len(pro_array),len(enh_array))
for index in range(0,len(enh_array),1):
    enh_array[index] = enh_array[index].replace(',yes', '')
    enh_array[index] = enh_array[index].replace(',no', '')

with open('NHEK/sample_feacture/NHEK_enhencers_result.txt','w') as output:
    # 每一次走两步
    for index in range(0,2,1):
        output.write(enh_array[index])
        output.write('\n')
    for index in range(1, 261, 1):
        output.write('@attribute f.%s numeric'%(index))
        output.write('\n')
    for index in range(6, 9, 1):
        output.write(enh_array[index])
        output.write('\n')

    for index in range(9, len(enh_array), 1):
        output.write(enh_array[index])
        output.write(',')
        output.write(pro_array[index+252])
        output.write('\n')

promoters.close()
enhancers.close()


"""----------------------------------"""
#合并增强子Kmer,NAC提取的特征
promoters = open('NHEK/sample_feacture/NHEK_promoters_Kmer.weka')
enhancers = open('NHEK/sample_feacture/NHEK_promoters_NAC.weka')
pro_array = promoters.read().split('\n')[:-1]
enh_array = enhancers.read().split('\n')[:-1]
print('data_length:',len(pro_array),len(enh_array))
for index in range(0,len(enh_array),1):
    enh_array[index] = enh_array[index].replace(',yes', '')
    enh_array[index] = enh_array[index].replace(',no', '')

with open('NHEK/sample_feacture/NHEK_promoters_result.txt','w') as output:
    # 每一次走两步
    for index in range(0,2,1):
        output.write(enh_array[index])
        output.write('\n')
    for index in range(1, 261, 1):
        output.write('@attribute f.%s numeric'%(index))
        output.write('\n')
    for index in range(6, 9, 1):
        output.write(enh_array[index])
        output.write('\n')

    for index in range(9, len(enh_array), 1):
        output.write(enh_array[index])
        output.write(',')
        output.write(pro_array[index+252])
        output.write('\n')

promoters.close()
enhancers.close()



"""----------------------------------"""
#合并增强子启动子样本
promoters = open('NHEK/sample_feacture/NHEK_promoters_result.txt')
enhancers = open('NHEK/sample_feacture/NHEK_enhencers_result.txt')
pro_array = promoters.read().split('\n')[:-1]
enh_array = enhancers.read().split('\n')[:-1]
print('data_length:',len(pro_array),len(enh_array))
for index in range(0,len(enh_array),1):
    enh_array[index] = enh_array[index].replace(',yes', '')
    enh_array[index] = enh_array[index].replace(',no', '')


#%%
with open('NHEK/result/NHEK_EP_extract.weka','w') as output:
    for index in range(0,2,1):
        output.write(enh_array[index])
        output.write('\n')
    for index in range(1, 521, 1):
        output.write('@attribute f.%s numeric'%(index))
        output.write('\n')
    for index in range(262,265,1):
        output.write(enh_array[index])
        output.write('\n')
    for index in range(265, len(enh_array), 1):
        output.write(enh_array[index])
        output.write(',')
        output.write(pro_array[index])
        output.write('\n')
promoters.close()
enhancers.close()