import docker
import typer


def info():
    client = docker.from_env()
    typer.echo(client.version())


def main():
    typer.run(info)


if __name__ == "__main__":
    main()
