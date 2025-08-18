# Robustness Assessment of the Open vSwitch Kernel Module

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This repository contains the artifacts of the paper accepted at the 36th IEEE International Symposium on Software Reliability Engineering ([ISSRE 2025](https://issre.github.io/2025/)).

## Abstract

Open vSwitch is a software implementation of a multilayer switch designed for virtualized environments. Its architecture includes components in both user and kernel space. Although Open vSwitch is considered to be a mature project and has been widely adopted, its robustness has never been publicly assessed. While previous works focused on performance, in this work, we investigate the robustness of a fundamental component of Open vSwitch, the kernel module. The approach is based on injecting faults into the control plane interface of the Open vSwitch kernel module - which is based on Netlink sockets. We systematically tested all Generic Netlink families implemented by Open vSwitch and their respective commands and attributes across four different Linux kernel versions. Results reveal a plethora of failures and clear indications of inconsistencies in the handling of faulty inputs.

## Getting started

Before using the resources in this repository, we strongly recommend reading the full paper accepted at ISSRE 2025. In that document, we briefly described the Open vSwitch architecture and presented in detail the Netlink-based interface of its kernel module, as well as our proposed approach to assessing its robustness.

### Repository structure overview

The contents of this repository are organized as follows.

```
.
├── experiments     # results and instructions for reproducing the experiments
├── src             # source code directory
├── .gitignore      # lists files that should be ignored by git
├── LICENSE         # the license file
├── README.md       # (this) general instructions
```

Each of the directories listed above contains several files, including a README.md file with detailed information and usage instructions.

### Reproducing the experiments

For detailed instructions on how to reproduce the experiments in the paper, please refer to the README.md file in the ["experiments/"](experiments/) directory.

## Citation

If you use the content of this repository, please cite our paper:

- J. Flauzino, M. Vieira, and E. P. Duarte Jr, "Robustness Assessment of the Open vSwitch Kernel Module," in the 36th IEEE International Symposium on Software Reliability Engineering (ISSRE 2025), 2025.

```
@inproceedings{flauzino2025robustness,
  title={{Robustness Assessment of the Open vSwitch Kernel Module}},
  author={Flauzino, Jos{\'e} and Vieira, Marco and Duarte Jr, Elias P},
  booktitle={36th IEEE International Symposium on Software Reliability Engineering (ISSRE, 2025)},
  year={2025}
}
```

Additionally, consider showing your support by starring ( :star: ) this repository.

## License

This project is licensed under the GNU License - see the [LICENSE](LICENSE) file for more details.

## Contact

For questions or comments, please contact José Flauzino ([jwvflauzino@inf.ufpr.br](mailto:jwvflauzino@inf.ufpr.br)).

