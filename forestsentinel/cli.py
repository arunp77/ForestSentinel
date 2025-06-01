import click
from forestsentinel.core.ingestion import download_data
from forestsentinel.core.preprocessing import preprocess_data
from forestsentinel.core.analysis import analyze_vegetation

@click.group()
def main():
    """ForestSentinel - Satellite-based deforestation monitoring tool"""
    pass

@main.command()
@click.option('--config', default='configs/default.yaml', help='Configuration file')
def ingest(config):
    """Download and prepare satellite data"""
    click.echo(f"Starting data ingestion with config: {config}")
    download_data(config)
    click.echo("Data ingestion complete")

@main.command()
@click.option('--config', default='configs/default.yaml', help='Configuration file')
def preprocess(config):
    """Preprocess satellite data"""
    click.echo(f"Starting preprocessing with config: {config}")
    preprocess_data(config)
    click.echo("Preprocessing complete")

@main.command()
@click.option('--config', default='configs/default.yaml', help='Configuration file')
@click.option('--aoi', required=True, help='Area of interest GeoJSON file')
def analyze(config, aoi):
    """Analyze vegetation changes"""
    click.echo(f"Starting analysis for AOI: {aoi}")
    analyze_vegetation(config, aoi)
    click.echo("Analysis complete")

@main.command()
@click.option('--config', default='configs/default.yaml', help='Configuration file')
def visualize(config):
    """Generate visualizations"""
    click.echo("Generating visualizations")
    # Visualization code here
    click.echo("Visualizations saved to output/")

if __name__ == "__main__":
    main()
