#!/bin/bash
mkdir out
Rscript string_data_download.r
gunzip -k ./out/*.gz
inp="$(ls ./out/*protein_links.tsv)"
python stringdb_parse.py  ${inp} ./out/parsed_out.txt
python pairwise_dis_index.py ./out/parsed_out.txt ./out/disconindex.txt
echo 
echo output - disconindex.txt
echo 
python pairwise_discon_vdisjoint_paths.py ./out/parsed_out.txt ./out/disjoint_path_discon_index.txt
echo 
echo output - disjoint_path_discon_index.txt
echo 
out="$(ls ./out/*__proteins.tsv)"
python mapping_on_annotation_file.py ./out/disjoint_path_discon_index.txt ${out} 
echo 
echo saved Result : Result_crucialnodes.txt  
echo saved Result : Result_noncrucialnodes.txt 
echo saved Result : Result_moderatenodes.txt
echo 
mv  Result_crucialnodes.txt Result_noncrucialnodes.txt Result_moderatenodes.txt ./out
