#!/usr/bin/env python3

class Person:
    jobs = [
        "Admin",
        "Finance",
        "Customer Service",
        "Sales",
        "Human Resources",
        "General Management",
        "ITC",
        "Research & Development",
        "Production",
        "Marketing",
        "Legal",
        "Purchasing"
    ]

    def get_name(self):
        pass
        return self._name

    def set_name(self, name):
        pass
        if (type(name) == (str)) and (1 <= len(name) <= 25):
            self._name = name.title()
        
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_job(self):
        pass
        return self._job

    def set_job(self, job):
        pass
        if (job in self.jobs):
            self._job = job

        else:
            print("Job must be in list of approved jobs.")

    name = property(get_name, set_name)
    job = property(get_job, set_job)