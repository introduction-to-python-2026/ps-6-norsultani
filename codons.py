def create_codon_dict(filepath):
  codons_and_aminoacids = {}

  with open(filepath, "r") as thefile:
    rows = thefile.readlines()

  for word in rows: 
   x = word.strip().split("\t")
   codons_and_aminoacids[x[0]] = x[2]

  return codons_and_aminoacids
