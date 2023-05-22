from threading import Thread

class Executor(Thread):
    def __init__(self, id, task_list, execution):
        super().__init__()
        self.id = id
        self.task_list = task_list
        self.execution = execution

    def run(self):
        while True:
            try:
                task = self.task_list.pop()
                # Magia --> Dame la referencia al metodo self.execution dentro del
                # objeto Tarea, en este caso es test, así que referenciará a test()
                funct_2_exec = getattr(task, self.execution)
                # Aquí la ejecutamos con parentesis
                funct_2_exec()
                print(getattr(task, self.execution))
            except IndexError:
                return

class PoolExecutors():
    def __init__(self, num_executors, task_list, execution):
        self.num_executors = num_executors
        self.task_list = task_list
        self.execution = execution
        self.executors = []

    def work(self):
        for w in range(self.num_executors):
            new_ex = Executor(w, self.task_list,self.execution)
            self.executors.append(new_ex)
            new_ex.start()

    # Funcion que avisa cuando se haya finalizado el trabajo, mientras haya trabajadores
    # vivos no mostrar
    def work_finished(self):
        for exec in self.executors:
            exec.join()

