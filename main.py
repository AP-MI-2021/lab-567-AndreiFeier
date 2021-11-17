from repository.repo import CRepo
from service.c_service import CService
from ui.console import Console

repo=CRepo()
service=CService(repo)
ui=Console(service)
ui.start()