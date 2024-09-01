"""Console script for llm_vs_llm_debate_toolkit."""


import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("llm-vs-llm-debate-toolkit")
    click.echo("=" * len("llm-vs-llm-debate-toolkit"))
    click.echo("Framework for running multi-turn debate between LLMs")


if __name__ == "__main__":
    main()
    
