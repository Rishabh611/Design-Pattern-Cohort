# Decorator design pattern

1. what;
    - decorator for objects
    - to enhance functionality without changing the underlying object
2. when, why
    - when you need to enhance functionality without changing the underlying object
3. strategy to implement
    - both decorator and decorated should implement a common interface
    - decorator should take the decorated object as argument.(aggregate)
4. implementation
'''
class Notify(ABC):
    @abstractmethod
    def notify():
        pass

class EmailNotification(Notify):
    def __init__(self, email_id):
        self.email_id = email_id
    def notify(self):
        print('send notification to {self.email_id}')

class FacebookNotification(Notify):
    def __init__(self, notifier: Notify, fb_id):
        self.notifier = notifier
        self.facebook_id = fb_id
    def notify(self):
        print('send FB notification')
        self.notifier.notify()

def caller_func():
    email_notifier = EmailNotification('user@email.com')
    fb_notifier = FacebookNotification(email_notifier, some_fb_id)
    fb_notifier.notify()
'''




'''
Decorator in Python world
limitation - it works only for functions

def my_logger(f):
    logger.info('accessed at now')
    def inner_funct(f):
        return f


@my_logger # kind of function of function, the decorated function is executed within the decorator function
def my_funct():
    pass


def caller():
    my_fucnt()
'''