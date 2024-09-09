from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import EditCourseView, GetCourseView, ShowCourseView, StoreCourseView, EnrollCourseView, GetCategoriesView, CompleteLectureView, StoreLessonView, StoreLectureView, StoreFilesView, StoreQuestionsView, StoreUserView, GetUserView, MyCoursesView, UpdateCourseImageView, UpdateCourseInstructorAvatarView, StoreAnswerView, UpdateCorrectAnswerView, CompleteCourseView, SearchCourseView, RemoveCourseView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signIn/', TokenObtainPairView.as_view(), name='signIn'),
    path('signUp', StoreUserView.as_view(), name='storeUser'),
    path('getUser/', GetUserView.as_view(), name='getUser'),
    path('getCourses/<int:category>/<int:count>/<int:page>/', GetCourseView.as_view(), name='getCourse'),
    path('myCourses/<int:category>/<int:count>/<int:page>/', MyCoursesView.as_view(), name='myCourses'),
    path('searchCourse/<int:count>/<int:page>/', SearchCourseView.as_view(), name='searchCourse'),
    path('storeCourse', StoreCourseView.as_view(), name='storeCourse'),
    path('editCourse/<int:id>/', EditCourseView.as_view(), name='editCourse'),
    path('updateCourse/<int:id>/', StoreCourseView.as_view(), name='updateCourse'),
    path('updateCourseImage/<int:id>/', UpdateCourseImageView.as_view(), name='updateCourseImage'),
    path('updateCourseInstructorAvatar/<int:id>/', UpdateCourseInstructorAvatarView.as_view(), name='updateCouseInstructorAvatar'),
    path('deleteCourse/<int:id>/', RemoveCourseView.as_view(), name='deleteCourse'),
    path('showCourse/<int:id>/', ShowCourseView.as_view(), name='showCourse'),
    path('enrollCourse/<int:id>/', EnrollCourseView.as_view(), name='enrollCourse'),
    path('completeLecture/', CompleteLectureView.as_view(), name='completeLecture'),
    path('completeCourse/', CompleteCourseView.as_view(), name='completeCourse'),
    path('storeLesson', StoreLessonView.as_view(), name='storeLesson'),
    path('updateLesson/<int:id>/', StoreLessonView.as_view(), name='updateLesson'),
    path('deleteLesson/<int:id>/', StoreLessonView.as_view(), name='deleteLesson'),
    path('storeLecture', StoreLectureView.as_view(), name='storeLecture'),
    path('updateLecture/<int:id>/', StoreLectureView.as_view(), name='updateLecture'),
    path('deleteLecture/<int:id>/', StoreLectureView.as_view(), name='deleteLecture'),
    path('storeFiles', StoreFilesView.as_view(), name='storeFiles'),
    path('deleteFile/<int:id>/', StoreFilesView.as_view(), name='deleteFile'),
    path('storeQuestion', StoreQuestionsView.as_view(), name='storeQuestion'),
    path('updateQuestion/<int:id>/', StoreQuestionsView.as_view(), name='updateQuestion'),
    path('deleteQuestion/<int:id>/', StoreQuestionsView.as_view(), name='deleteQuestion'),
    path('storeAnswer/', StoreAnswerView.as_view(), name='storeAnswer'),
    path('updateAnswer/<int:id>/', StoreAnswerView.as_view(), name='updateAnswer'),
    path('updateCorrectAnswer/<int:lid>/<int:aid>/', UpdateCorrectAnswerView.as_view(), name='updateCorrectAnswer'),
    path('deleteAnswer/<int:id>/', StoreAnswerView.as_view(), name='deleteAnswer'),
    path('getCategories/', GetCategoriesView.as_view(), name='getCategories'),
    path('payments/', include('djstripe.urls', namespace="djstripe")),
]

urlpatterns = format_suffix_patterns(urlpatterns)
