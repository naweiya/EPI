initialData 是六个细胞系的原始数据
pos_neg.py 将原始数据划分为正负样本
sample_bind.py 进行采样，并且将采样完的正负样本合起来
feactureBind _allBind.py 将不同的特征合起来，并且将启动子增强子的特征合起来

特征提取：https://github.com/Superzchen/iLearn
python iLearn-nucleotide-basic.py --file Hela/sample_feacture/Hela_enhancers_sample.fasta --method Kmer --format weka --out Hela/sample_feacture/Hela_enhencers_Kmer
python iLearn-nucleotide-basic.py --file Hela/sample_feacture/Hela_promoters_sample.fasta --method Kmer --format weka --out Hela/sample_feacture/Hela_promoters_Kmer
python iLearn-nucleotide-basic.py --file Hela/sample_feacture/Hela_enhancers_sample.fasta --method NAC --format weka --out Hela/sample_feacture/Hela_enhencers_NAC
python iLearn-nucleotide-basic.py --file Hela/sample_feacture/Hela_promoters_sample.fasta --method NAC --format weka --out Hela/sample_feacture/Hela_promoters_NAC


特征选择+分类器：https://www.cs.waikato.ac.nz/ml/weka/


