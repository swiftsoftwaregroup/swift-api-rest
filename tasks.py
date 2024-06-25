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
def update_client_ng(ctx):
    """Update the TypeScript client code in `../swift-api-rest-ng`"""
    ctx.run("./scripts/update-client-ng.sh", pty=True)

@task
def update_client_react(ctx):
    """Update the TypeScript client code in `../swift-api-rest-react`"""
    ctx.run("./scripts/update-client-react.sh", pty=True)
