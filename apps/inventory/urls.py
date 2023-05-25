from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("home/", login_required(Home.as_view()), name="home"),
    path("home/<int:pk>", login_required(Home.as_view()), name="home_with_id"),
    path("import-picture-file/", login_required(ImportPictureFile.as_view()),
        name="import-picture-file"),
    path("import-stock-list/", login_required(ImportStockList.as_view()),
        name="import-stock-list"),
    path("export-picture-result/", login_required(ExportPictureResult.as_view()),
        name="export-picture-result"),
    path("import-worker-batch-csv/", login_required(ImportWorkerBatch.as_view()),
        name="import-worker-batch-csv"),
    path("no-match-available/", login_required(NoMatchAvailableView.as_view()),
        name="no-match-available"),
    path("move-to-end-of-queue/", login_required(MoveToEndOfQueueView.as_view()),
        name="move-to-end-of-queue"),
    path("difficult-to-read/", login_required(DifficultToReadView.as_view()),
        name="difficult-to-read"),
    path("inferred-info/", login_required(InferredInfoView.as_view()),
        name="inferred-info"),
    path("change-button/", login_required(ChangeButtonView.as_view()),
        name="change-button"),
    path("batch-status/", login_required(BatchStatusView.as_view()),
        name="batch-status"),
    path("recent-matches/", login_required(RecentMatchesView.as_view()),
        name="recent-matches"),
    path("export-batch-result/", login_required(ExportBatchResult.as_view()),
        name="export-batch-result"),
    path("match-stock-id/", login_required(StockIdBtnClickView.as_view()),
        name="match-stock-id")
]