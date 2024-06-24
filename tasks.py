# see: http://docs.pyinvoke.org/en/stable/
from invoke import task


@task
def podman(ctx):
    """Recreate the image and the container in podman"""
    ctx.run("./scripts/podman.sh", pty=True)


@task
def podman_delete(ctx):
    """Delete the container and the image in podman"""
    ctx.run("./scripts/podman-delete.sh", pty=True)


@task
def update_typescript_client(ctx):
    """Update the TypeScript client code in `../swift_api_client`"""
    ctx.run("./scripts/update-typescript-client.sh", pty=True)
