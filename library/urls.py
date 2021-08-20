from django.urls import path

from . import views
from .views import BookDetailView, BookListView, BookCreateView, BookUpdateView, ProposalListView, OwnedBooksListView, ApproveProposalView, RejectProposalView, ProposalCreateView

urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('proposals/', ProposalListView.as_view(), name='proposals'),
    path('proposals/new_proposal/', ProposalCreateView.as_view(), name='new_proposal'),
    path('proposals/<int:pk>/approve/', ApproveProposalView.as_view(), name='proposal_approve'),
    path('proposals/<int:pk>/reject/', RejectProposalView.as_view(), name='proposal_reject'),
    path('my-books/', OwnedBooksListView.as_view(), name='my_books'),
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='update'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('books/add/', BookCreateView.as_view(), name='add'),
]
