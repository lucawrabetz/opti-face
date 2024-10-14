import os

from optiface import ui
from optiface.core import iinstance
from optiface.datamodel import feature


# - experiment configuration
# - receive, in public method configure():
#   - instance ids (not instances for memory) to be solved
#   - solver ids to solve them with
# - for more complex setup, will take care of outside (at creation & call site of) ComputationExperiment
# - user will be able to call the experiment controller service and request multiple experiments
# - this simplifies the design of a single experiment - it can be simple as the user can create complexity by running multiple experiments, so, here are the invariants for us:
#   - all solvers requested solve all instances requested
# - both instances and solver ids could be maintained as sets of parameters to combine, but it doesn't really make sense for the instance ids as you could make up / ask for parameter combinations that don't exist in the saved instances, so we'll start with the following for each (instance, solver):
#   - starting with a set of selected set_names, assume all instances in set selected
#   -
# id public method, run():
# - read each instance, and for each


class ComputationalExperiment:
    def configure(
        self,
        instance_pathidpairs: list[feature.PathIdPair],
        solver_ids: list[feature.FeatureValueDict],
        instance: iinstance.IInstance,
    ) -> None:
        ui.header("Configuring Experiment [opti-face]")
        self.instance_pathidpairs: list[feature.PathIdPair] = instance_pathidpairs
        self.solver_ids: list[feature.FeatureValueDict] = solver_ids
        self.instance: iinstance.IInstance = instance

    def single_run(self, solver_id: feature.FeatureValueDict) -> None:
        ui.body("In a single run [opti-face]...")
        solver_description: str = ", ".join([str(k[1]) for k in solver_id.values()])
        ui.separator_line()
        ui.body(f"Running {solver_description} on {self.instance.filepath} [opti-face]")

    def run(self) -> None:
        ui.subheader("Running an experiment [opti-face]...")
        for filepath, parameters in self.instance_pathidpairs:
            self.instance.configure(parameters, filepath)
            self.instance.read()
            ui.separator_line()
            for solver_id in self.solver_ids:
                self.single_run(solver_id)
                self.instance.reset()
                ui.separator_line()
