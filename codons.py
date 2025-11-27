def create_codon_dict(file_path):
  codons_and_aminoacids = {}

  for word in rows: 
   x = word.strip().split("\t")
   codons_and_aminoacids[x[0]] = x[2]

  return codons_and_aminoacids

