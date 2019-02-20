if __name__ == '__main__':
    print("RUN")
    import os
    import sys


    print(sys.path)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'langProject.settings')

    from django.core.wsgi import get_wsgi_application

    application = get_wsgi_application()

    from captions.models import Caption


    #from captions.models import Caption
    t = Caption(video_id='UID', start_time='000', end_time='124', caption='Captions This is')
    print(Caption.objects.all())
