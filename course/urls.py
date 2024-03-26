from django.urls import path
from course.views import *

urlpatterns = [
    path('category/', CategoryListCreate.as_view(), name='category-list-create'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-retrieve-update-destroy'),   
    
    path('cours/', CoursListCreate.as_view(), name='cours-list-create'),
    path('cours/<int:pk>/', CoursRetrieveUpdateDestroy.as_view(), name='cours-retrieve-update-destroy'),
   
    path('modules/', ModuleListCreate.as_view(), name='module-list-create'),
    path('modules/<int:pk>/', ModuleRetrieveUpdateDestroy.as_view(), name='module-retrieve-update-destroy'),
    
    path('lecons/', LeconListCreate.as_view(), name='lecon-list-create'),
    path('lecons/<int:pk>/', LeconRetrieveUpdateDestroy.as_view(), name='lecon-retrieve-update-destroy'),
   
    path('contenu-image/', ContenuImageListCreate.as_view(), name='contenu-image-list-create'),
    path('contenu-image/<int:pk>/', ContenuImageRetrieveUpdateDestroy.as_view(), name='contenu-image-retrieve-update-destroy'),

    path('contenu-texte/', ContenuTexteListCreate.as_view(), name='contenu-texte-list-create'),
    path('contenu-texte/<int:pk>/', ContenuTexteRetrieveUpdateDestroy.as_view(), name='contenu-texte-retrieve-update-destroy'),

    path('contenu-audio/', ContenuAudioListCreate.as_view(), name='contenu-audio-list-create'),
    path('contenu-audio/<int:pk>/', ContenuAudioRetrieveUpdateDestroy.as_view(), name='contenu-audio-retrieve-update-destroy'),

    path('contenu-video/', ContenuVideoListCreate.as_view(), name='contenu-video-list-create'),
    path('contenu-video/<int:pk>/', ContenuVideoRetrieveUpdateDestroy.as_view(), name='contenu-video-retrieve-update-destroy'),
    
    path('inscriptions/', InscriptionListCreate.as_view(), name='inscription-list-create'),
    path('inscriptions/<int:pk>/', InscriptionRetrieveUpdateDestroy.as_view(), name='inscription-retrieve-update-destroy'),
   
    path('commentaires/', CommentaireListCreate.as_view(), name='commentaire-list-create'),
    path('commentaires/<int:pk>/', CommentaireRetrieveUpdateDestroy.as_view(), name='commentaire-retrieve-update-destroy'),
]
