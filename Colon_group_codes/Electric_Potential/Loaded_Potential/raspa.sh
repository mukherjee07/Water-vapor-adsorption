#!/bin/bash
if [ -r /opt/crc/Modules/current/init/bash ]; then
        source /opt/crc/Modules/current/init/bash
fi
# Source global definitions
if [ -f /etc/bashrc ]; then
        . /etc/bashrc
fi

module load python
cd /scratch365/kmukherj/Charged_Cylinders/10.09.2020/Potential_plots/9.24Ansgtorm/Inner/fract_Z/
python frac_potential.py
