&#x20;  # Lab 2 - SDN controllers, OpenFlow 1.3 and topology discovery



&#x20;  M2 CNS - Universite d'Evry / Universite Paris-Saclay.



&#x20;  ## Content



&#x20;  | Exercise | Topic | Files |

&#x20;  |---|---|---|

&#x20;  | 1 | Simple-tree data center topology (Mininet high-level and low-level API) | `scripts/simpletree\_highlevel.py`, `scripts/simpletree\_lowlevel.py` |

&#x20;  | 2 | Network with a loop, no spanning tree (broadcast storm) | `scripts/loop.py` |

&#x20;  | 3 | OpenFlow 1.3 messages between Ryu and Open vSwitch | Wireshark analysis |

&#x20;  | 4 | dpctl, ovs-ofctl, ovs-dpctl | command line |

&#x20;  | 5 | Topology discovery (LLDP/BDDP) with OpenDaylight and ONOS | Wireshark analysis |

&#x20;  | 6 | Switching rules and flow timeouts | Wireshark analysis |



&#x20;  ## Run the scripts (Mininet VM, Ubuntu 20.04)



```bash

&#x20;  sudo python3 scripts/simpletree\_highlevel.py 2

&#x20;  sudo python3 scripts/simpletree\_lowlevel.py 2

&#x20;  sudo python3 scripts/loop.py

```



&#x20;  The argument is the value of n. Clean up between runs with `sudo mn -c`.



&#x20;  Warning: `loop.py` creates a broadcast storm. Keep the test short.

