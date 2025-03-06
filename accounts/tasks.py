from celery import shared_task
# from time import sleep
from blog.models import Post

@shared_task
def delete_done_post():
    Post.objects.filter(status=True).delete()
    print("Successfully deleted done posts!")
    # posts.delete()
    # posts.save()
    # print('post deleted done')
    # for post in posts:
    #     print(post.title)










# @shared_task
# def send_email():
#     sleep(3)
#     print('done sending email')



# wrong implementation
# from core.celery import Celery
# @Celery.task
# def send_email():
#     sleep(3)
#     print('done sending email')


