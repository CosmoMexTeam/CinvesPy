import luigi
import time


# Meta Task
class TaskExample(luigi.Task):
    filename = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget('../outputs/{}.txt'.format(self.filename))

    def run(self):
        time.sleep(5)
        with self.output().open('w') as outfile:
            outfile.write('DONE!')

# DAG
class TaskA(TaskExample):
    def requires(self):
        return None

class TaskG(TaskExample):
    def requires(self):
        return None

class TaskB(TaskExample):
    def requires(self):
        return TaskA('A')

class TaskC(TaskExample):
    def requires(self):
        return TaskB('B')

class TaskD(TaskExample):
    def requires(self):
        return [TaskB('B'), TaskG('G')]

class TaskE(TaskExample):
    def requires(self):
        return [TaskC('C'), TaskB('B'), TaskD('D')]

class TaskF(TaskExample):
    def requires(self):
        return TaskE('E')

class AllTasks(luigi.WrapperTask):
    def requires(self):
        return TaskF('F')
