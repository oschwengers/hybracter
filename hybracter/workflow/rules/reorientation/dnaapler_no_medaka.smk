"""
dnaapler no medaka
"""


rule dnaapler_no_medaka:
    """
    Runs dnaapler to begin chromosome with dnaa when medaka isn't called
    """
    input:
        fasta=os.path.join(
            dir.out.chrom_pre_polish, "{sample}_chromosome_plus_plasmids.fasta"
        ),
    output:
        fasta=os.path.join(dir.out.dnaapler, "{sample}", "{sample}_reoriented.fasta"),
        version=os.path.join(dir.out.versions, "{sample}", "dnaapler.version"),
    conda:
        os.path.join(dir.env, "dnaapler.yaml")
    params:
        dir=os.path.join(dir.out.dnaapler, "{sample}"),
    resources:
        mem_mb=config.resources.med.mem,
        mem=str(config.resources.med.mem) + "MB",
        time=config.resources.med.time,
    threads: config.resources.med.cpu
    benchmark:
        os.path.join(dir.out.bench, "dnaapler", "{sample}.txt")
    log:
        os.path.join(dir.out.stderr, "dnaapler", "{sample}.log"),
    shell:
        """
        dnaapler all -i {input.fasta} -o {params.dir} -p {wildcards.sample} -t {threads} -a nearest -f 2> {log}
        dnaapler --version > {output.version}
        """


rule dnaapler_extract_intermediate_assembly:
    """
    extracts the reoriented prepolished chrom assembly
    """
    input:
        fasta=os.path.join(dir.out.dnaapler, "{sample}", "{sample}_reoriented.fasta"),
        completeness_check=os.path.join(dir.out.completeness, "{sample}.txt"),
    output:
        fasta=os.path.join(
            dir.out.dnaapler, "{sample}", "{sample}_reoriented_chromosome.fasta"
        ),
    params:
        min_chrom_length=getMinChromLength,
    conda:
        os.path.join(dir.env, "scripts.yaml")
    resources:
        mem_mb=config.resources.sml.mem,
        mem=str(config.resources.sml.mem) + "MB",
        time=config.resources.sml.time,
    threads: config.resources.sml.cpu
    script:
        os.path.join(dir.scripts, "extract_chromosome.py")
