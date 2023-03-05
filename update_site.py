from download_site import download_site
from deploy_to_ftp import deploy_to_ftp


def update_site(folder: str, site_url: str, ftp_host: str, ftp_user: str, ftp_pwd: str, force_download: bool):
    download_site(
        url=site_url,
        folder=folder,
        force_download=force_download
    )
    deploy_to_ftp(
        host=ftp_host,
        user=ftp_user,
        password=ftp_pwd,
        base_folder=folder
    )
