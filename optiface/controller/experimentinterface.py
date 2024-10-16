"""
Run a "single experiment" - all solvers selected solving all instances selected.

Classes:

    ComputationalExperiment
"""
from optiface import ui
from optiface.core import iinstance
from optiface.datamodel import feature


class ComputationalExperiment:
    """
    Class to run a set of solvers on a set of instances.
    """

    def configure(
        self,
        instance_path_id_pairs: list[feature.PathIdPair],
        solver_ids: list[feature.FeatureValueDict],
        instance: iinstance.IInstance,
    ) -> None:
        """Configure experiment by setting attributes to store instance names and locations, and solver ids."""
        ui.header("Configuring Experiment [opti-face]")
        self.instance_path_id_pairs: list[feature.PathIdPair] = instance_path_id_pairs
        self.solver_ids: list[feature.FeatureValueDict] = solver_ids
        self.instance: iinstance.IInstance = instance

    def single_run(self, solver_id: feature.FeatureValueDict) -> None:
        """Solve a single instance with a single solver."""
        ui.body("In a single run [opti-face]...")
        solver_description: str = ", ".join([str(k[1]) for k in solver_id.values()])
        ui.separator_line()
        ui.body(f"Running {solver_description} on {self.instance.filepath} [opti-face]")

    def run(self) -> None:
        ui.subheader("Running an experiment [opti-face]...")
        for filepath, parameters in self.instance_path_id_pairs:
            self.instance.configure(parameters, filepath)
            self.instance.read()
            ui.separator_line()
            for solver_id in self.solver_ids:
                self.single_run(solver_id)
                self.instance.reset()
                ui.separator_line()
