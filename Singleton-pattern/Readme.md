Singleton:
1. what it is
 - single instance of a class
 - globally shared
 - kind of a funnel, where requests get channelised and only 1 can access the resource
2. under what situation you can use: Why, when
 - resource heavy processes
 - handle mutability (read, write)
   - read: semaphore(n number of processes can access)
   - write: mutex(binary semaphore)(only 1 process can access), avoid race condition
 - db connections, caches, logger
3. What is the strategy for implementing it
 - private construtor # so that no one can make an instance of the class
 - a global entry point meaning a public method to access that private instance # to access the singleton object
 - private instance of the class
 - lazy loading vs eager/early loading
 - thread safety (double null check pattern - Concurrency pattern, acquire the lock as close as possible to the operation, particularly the write operation)
4. actual implementation
