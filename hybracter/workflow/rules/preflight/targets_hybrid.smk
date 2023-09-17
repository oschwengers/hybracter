"""
All target output files are declared here
"""

# need long read polish aggr file regardless even if no polish selected 
# because of dnaapler
"""
polca depends on --no_polca flag
"""

# Polca
if config.args.no_polca == True:
    polca_files = []
    
else:
    polca_files = os.path.join(dir.out.flags, "aggr_polca.flag")


"""
hybrid
"""

TargetFilesHybrid = [
    os.path.join(dir.out.flags, "aggr_qc.flag"),
    os.path.join(dir.out.flags, "aggr_assemble.flag"),
    os.path.join(dir.out.flags, "aggr_short_read_polish.flag"),
    os.path.join(dir.out.flags, "aggr_long_read_polish.flag"),
    polca_files,
    os.path.join(dir.out.flags, "aggr_plassembler.flag"),
    os.path.join(dir.out.flags, "aggr_combine_plassembler_info.flag"),
    os.path.join(dir.out.flags, "aggr_ale.flag"), 
    os.path.join(dir.out.flags, "aggr_final.flag")
]



"""
download 
"""

TargetFilesDownload = [
    os.path.join(dir.plassemblerdb,'plsdb.msh'),
    os.path.join(dir.plassemblerdb, 'plsdb.tsv')
]

