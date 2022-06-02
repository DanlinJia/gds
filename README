1.0.0, June 2021

GDS README

GPUDirect Storage Installation and Usage
-----------------------------------------

I. Validated Software and Hardware Configuration
========================================================

GPUDirect Storage software package has been tested with the following SW configurations and hardware platforms. RHEL8.3 support is released at Alpha level. It has been tested on OEM systems with NVMe protocol and released for experimental purposes. 

Tested on NVIDIA DGX-1, DGX-2, and DGX A100 platforms.
Tested to work on following GPUs: NVIDIA Ampere architecture based GPUs Ampere(A100), Turing (T4) Volta (V100) and Pascal (P100) architectures

Ubuntu distribution (tested with specific Linux kernel versions)
	18.04 (bionic) - 4.15.0-135
	20.04 (focal) - 5.4.0-42 till 5.4.0-72
RHEL8.3        - 4.18.X
DGX OS 5.0.5   - 5.4.0-42 till 5.4.0-72

Tested with NVIDIA driver versions 418.116.00 and 450.80.02 and CUDA runtime versions 10.1, 10.2, 11.0, 11.1, 11.2.
Expected to work with NVIDIA driver version 418.116.00 and above.

Tested on MOFED versions 
MLNX_OFED_LINUX-5.1-2.5.8.0, >= 5.2-2.2.3.0 and 5.3-1.0.0.1
**Important**:
Please install MOFED (refer to section VIII) prior to installing GDS. This is required for making sure that GDS has support for Local and Distributed File Systems. This step is NOT necessary on DGX servers where MOFED is already installed. Note that the version of MOFED will be upgraded to a compatible version as part of the installation.


Tested only on 64-bit applications and platforms.

Supported on Lustre EXAScaler 5.1 and above and tested with client versions - 2.12.3_ddn29, 2.12.3_ddn39, 2.12.5_ddn4, 2.12.6_ddn3. RHEL8.3 support in ExaScaler 5.2.1 and above.

The supported WekaFS version is 3.8.0. Experimental support for GDS writes is available on 3.9.0 and above.

The supported VAST version is 3.2.1 and above.

Supported on IBM SpectrumScale version 5.1.1. Only GDS reads are supported, writes use posix IO.

Tested using third-party library versions:
     libudev: libudev.so.1
     liburcu: liburcu.so.6 or liburcu.so.1
     libmount: libmount.so.1
     libnuma: libnuma.so.1
     libcrypto: libcrypto.so.1.1 or libcrypto.so.10

Supported cuFile Packages:
Ubuntu 18.04: CUDA 10.1 - present (CUDA 11.2)
Ubuntu 20.04: CUDA 11.0 - present (CUDA 11.2)
RHEL     8.3: CUDA 11.0 - present (CUDA 11.2)

The support matrix for official NVIDIA driver packaging is

Ubuntu 18.04: 410, 418, 440, 450, 455, 460
Ubuntu 20.04: 450, 455, 460

RHEL     8.3: 460

II. MOFED Installation (Non DGX platforms)
==========================

Please download a MOFED version from the official Mellanox website. This step is NOT necessary on the DGX platform.
1. Extract the MOFED package and change to the installation directory.
2a. MOFED 5.1 $ ./mlnxofedinstall --with-nvmf --with-nfsrdma --enable-gds --add-kernel-support
2b. MOFED 5.3 $ ./mlnxofedinstall --with-nvmf --with-nfsrdma --add-kernel-support
Note: For RHEL 8.3, you have to use MOFED 5.3 and add flag “--kmp”
3. For Ubuntu - $update-initramfs -u -k `uname -r`
   For RHEL   - $dracut -f
4. Restart your system in the current Linux Kernel version which you plan to use for GDS.

III. Prepare the OS for DGX BaseOS 
==================================
      NVSM and MOFED packages can be installed via network using preview network repository. 
      At this point ONLY DGX OS 5.0 (UB20.04) is supported on the DGX platform. 

      Note:
           If you have CUDA toolkit installed then note down the currently used 
           toolkit version and specify it as <x> in step 9. Start with step 2 onwards. 

           If you do not have CUDA toolkit installed then run command below:

           $ nvidia-smi -q | grep CUDA | awk '{print $4}' | sed 's/\./-/'
             replace <x> in step 1 and step 9 with output from command line above.

      Steps:
	    1. sudo apt-get install cuda-toolkit-<x>
            2. sudo apt-key adv --fetch-keys https://repo.download.nvidia.com/baseos/GPG-KEY-dgx-cosmos-support
            3. sudo add-apt-repository "deb https://repo.download.nvidia.com/baseos/ubuntu/focal/x86_64/ focal-updates preview"
            4. sudo apt update
            5. sudo apt full-upgrade -y
            6. sudo apt install mlnx-ofed-all mlnx-nvme-dkms
            7. sudo update-initramfs -u -k `uname -r`
            8. sudo reboot
 
IV. GPUDirect Storage Installation Steps
========================================

Notes: 

a) Make sure the machine has access to the network for downloading additional packages using Ubuntu APT/ Redhat RPM, YUM and DNF packaging software (advance packaging tool).  
b) Please make sure the NVIDIA driver is installed using the Ubuntu APT/Redhat RPM, YUM and DNF   package manager. NVIDIA drivers installed using NVIDIA-Linux-x86_64.<version>.run file are NOT supported with the nvidia-gds package.
c) In this document, cuda-<x>.<y>, x refers to CUDA major version and y refers to a minor version.


1. Removal of prior gds installation on Ubuntu systems:

   If any older GDS release packages are installed, please use the following steps prior to upgrading to 1.0.0 release.

      If you have 0.8.0, do:
        $ sudo dpkg --purge nvidia-fs
        $ sudo dpkg --purge gds-tools
        $ sudo dpkg --purge gds
   If you have 0.9.0 or above, do:
        $ sudo apt-get remove --purge nvidia-gds
        $ sudo apt-get autoremove

2. GDS Package Installation

        GPUDirectStorage(GDS) packages can be installed using CUDA packaging guide.
        In order to use GDS is necessary to install the CUDA package and MOFED package.
        Instructions to install CUDA can be found here.
        https://docs.nvidia.com/cuda/cuda-installation-guide-linux/#package-manager-installation

        GDS is supported in two different modes: i
             GDS (default/full perf mode) - cufile libraries, GDS tools and nvidia-fs-dkms kernel module support. 
             Compatibility mode - only cufile libraries and GDS tools

        Installation instructions for them differ slightly.Compatibility mode is the only mode that is supported 
        on certain distributions due to SW dependency limitations.

        Full GDS support is restricted on following Linux distros:
                Ubuntu 18.04, 20.04, RHEL 8.3, RHEL 8.4
                To include all gds packages 

                        sudo apt-get install nvidia-gds 
                        or
                        sudo dnf install nvidia-gds
                         
        Compatibility mode* is supported on following Linux Distros:
                Note: Compatibility mode works with GDS qualified file systems.
                Debian 10, RHEL7.9, CentOS 7.9, Ubuntu – Desktop versions of 18.04 and 20.04
                SLES 15.2, OpenSUSE 15.2

                If you have not installed cuda then you will need to execute following command
                 to use GDS compatibility mode.

                        sudo apt-get install cuda 
                        or 
                        sudo dnf install cuda 

3.  Verify the package installation:

    On DGX OS and UbuntuOS:

       $ dpkg -s nvidia-gds

    Package: nvidia-gds
        Status: install ok installed
        Priority: optional
        Section: multiverse/devel
        Installed-Size: 7
        Maintainer: cudatools <cudatools@nvidia.com>
        Architecture: amd64
        Source: gds-ubuntu1804
        Version: 1.0.0.12-1
        Provides: gds
        Depends: libcufile0, gds-tools, nvidia-fs
        Description: Metapackage for GPUDirect Storage
        GPUDirect Storage metapackage

    On RHEL:

       $ rpm -qi nvidia-gds

	Name        : nvidia-gds
	Version     : 1.0.0
	Release     : 1
	Architecture: x86_64
	Install Date: Thu Jun 10 03:13:50 2021
	Group       : Unspecified
	Size        : 0
	License     : NVIDIA Proprietary
	Signature   : RSA/SHA512, Tue Mar 23 17:41:44 2021, Key ID f60f4b3d7fa2af80
	Source RPM  : nvidia-gds-1.0.0-1.src.rpm
	Build Date  : Tue Jun 9 17:41:43 2021
	Build Host  : cia-jenkins-agent-06.nvidia.com
	Relocations : (not relocatable)
	URL         : http://nvidia.com
	Summary     : GPU Direct Storage meta-package
	Description :
	Meta-package for GPU Direct Storage containing all the available packages required for libcufile and nvidia-fs.

4. Run gdscheck to verify GDS installation:

   Note:  Following command expects python3 to be present on the system. If it fails because of python3 not being available then you can invoke the command 
          with explicit path where python (i.e. python2) is installed.  e.g. /usr/bin/python /usr/local/cuda-<x>.<y>/gds/tools/gdscheck.py -p


        $ /usr/local/cuda-<x>.<y>/gds/tools/gdscheck.py -p

         GDS release version : 1.0.0.71
         nvidia_fs version:  2.7 libcufile version: 2.4
         ============
         ENVIRONMENT:
         ============
         =====================
         DRIVER CONFIGURATION:
         =====================
         NVMe               : Supported
         NVMeOF             : Supported
         SCSI               : Unsupported
         ScaleFlux CSD      : Unsupported
         NVMesh             : Unsupported
         DDN EXAScaler      : Unsupported
         IBM Spectrum Scale : Unsupported
         NFS                : Supported
         WekaFS             : Unsupported
         Userspace RDMA     : Unsupported
         --Mellanox PeerDirect : Enabled
         --rdma library        : Not Loaded (libcufile_rdma.so)
         --rdma devices        : Not configured
         --rdma_device_status  : Up: 0 Down: 0
         =====================
         CUFILE CONFIGURATION:
         =====================
         properties.use_compat_mode : true
         properties.gds_rdma_write_support : true
         properties.use_poll_mode : false
         properties.poll_mode_max_size_kb : 4
         properties.max_batch_io_timeout_msecs : 5
         properties.max_direct_io_size_kb : 16384
         properties.max_device_cache_size_kb : 131072
         properties.max_device_pinned_mem_size_kb : 33554432
         properties.posix_pool_slab_size_kb : 4 1024 16384
         properties.posix_pool_slab_count : 128 64 32
         properties.rdma_peer_affinity_policy : RoundRobin
         properties.rdma_dynamic_routing : 0
         fs.generic.posix_unaligned_writes : false
         fs.lustre.posix_gds_min_kb: 0
         fs.weka.rdma_write_support: false
         profile.nvtx : false
         profile.cufile_stats : 0
         miscellaneous.api_check_aggressive : false
         =========
         GPU INFO:
         =========
         GPU index 0 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 1 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 2 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 3 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 4 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 5 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 6 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 7 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 8 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 9 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 10 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 11 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 12 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 13 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 14 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         GPU index 15 Tesla V100-SXM3-32GB bar:1 bar size (MiB):32768 supports GDS
         ==============
         PLATFORM INFO:
         ==============
         IOMMU : disabled
         Platform verification succeeded        

   Note: There are READMEs provided in /usr/local/cuda-<x>.<y>/gds/tools and /usr/local/cuda-<x>.<y>/gds/samples to learn usage. 


V. Uninstalling gds 
========================================================

To uninstall from Ubuntu and DGX OS

        $ sudo apt remove --purge "nvidia-gds*"
        $ sudo apt-get autoremove

To uninstall from RHEL:

        $ sudo dnf remove "nvidia-gds*"
 
VI. GDS Library and Usage
=========================

GDS cuFile related library and header files are located at /usr/local/cuda-<x>.<y>/targets/x86_64-linux/lib. 

For example, /usr/local/cuda-11.2/targets/x86_64-linux/lib. 
/usr/local/cuda-<x>.<y>/targets/x86_64-linux/lib/libcufile.so : cuFile API library
/usr/local/cuda-<x>.<y>/targets/x86_64-linux/lib/libcufile_rdma.so : cuFile RDMA support library
/usr/local/cuda-<x>.<y>/targets/x86_64-linux/include/cufile.h :  cufile header file
/usr/local/cuda-<x>.<y>/targets/x86_64-linux/lib/libcufile_static.a : cuFile API static library
/usr/local/cuda-<x>.<y>/targets/x86_64-linux/lib/libcufile_rdma_static.a : cuFile RDMA support static library
 
VII. Sample Applications and Testing Tools
==========================================

Note: Make sure the cuda-runtime library (libcudart) is installed.

/usr/local/cuda-<x>.<y>/gds/tools : GDS basic data verification and io tools.
/usr/local/cuda-<x>.<y>/gds/samples : sample applications for cuFile API usage.
 
Please follow the steps in the README available under tools and samples for usage.
 
VIII. Mounting
========================================================

For distributed file systems (DFS), use the appropriate file-system mount command to mount the file system and verify the mount. For commands to mount specific DFS refer to the vendor-specific guide. 


For EXT4 over NVMe, NVMeOF 
#IMPORTANT: GDS is only supported on Ext4 filesystem mounted with ONLY data=ordered mode
 
EXAMPLE:
 
# lsblk | grep nvme
nvme0n1                      259:0        0   2.9T  0 disk
├─nvme0n1p1                  259:1        0         1M  0 part
├─nvme0n1p2                  259:2        0   2.9T  0 part
└─nvme0n1p3                  259:3        0  31.9G  0 part
 
mkdir -p /mnt/nvme
mount /dev/nvme0n1p2 -o data=ordered /mnt/nvme
 
$ mount | grep ext4 | grep nvme
/dev/nvme0n1p2 on /mnt/nvme type ext4 (rw,relatime,data=ordered)
 
IX. Integrating cuFile APIs with Applications
========================================================

You need the header file cufile.h, libcufile.so or libcufile_static.a for using cuFile APIs and additionally libcufile_rdma.so for supporting WekaIO filesystem and IBM SpectrumScale filesystems;
/usr/local/cuda-x.y/gds/samples/*.cc contains samples on the usage of cuFile APIs as per the cuFile API specification.
 

X. cuFile Configuration
========================================================

For cuFile configuration, a default global configuration file cufile.json is installed by the GDSinstaller with read privileges to the user, which contains IO path and Control path parameters.
Ways to configure:
1. An admin can update the global cufile.json based on the requirements.
 
2. Applications can also create a custom cuFile json configuration file by overriding the default settings and provide the file-path as an environment variable via 'export CUFILE_ENV_PATH_JSON=<filepath>'.
 
3. The environment variable CUFILE_LOGFILE_PATH is used to specify the file location to log the cuFile generated logs.
   For example, export CUFILE_LOGFILE_PATH=/home/mycufilelog, will log in /home/mycufilelog.
   This exported variable takes the highest priority for logging location which means that if this variable is set, then even if the log directory 'dir' is in cufile.json, the logging would take place only in the path specified by CUFILE_LOGFILE_PATH.
 
4. cuFile log file naming is changed if "logging":"dir" is specified in the cufile.json The pathname will be <dir>/cufile.log_<PID>_<time-stamp>.log.


XI. Adding udev rules for showing members of a raid volume in Redhat 8.3
==================================================================

As a sudo user change following line in 
/lib/udev/rules.d/63-md-raid-arrays.rules
IMPORT{program}="/usr/sbin/mdadm --detail --export $devnode" 
Reboot the node or restart the mdadm.

XII. GDS Support Information
=======================================================

Please follow the GDS Best Practices Guide and review the GDS Installation and Troubleshooting Guide before calling GDS support.
 
XIII. GDS Documentation
=======================================================
The latest docs will be available at https://docs.nvidia.com/gpudirect-storage/index.html
 
XIV. Known Issues
=======================================================
- nvidia.ko version 465.19.x version causes GDS to crash on process failures, use latest TRD nvidia driver version 460.73.01.
- nvidia_p2p_get_pages performance has severely regressed in NVIDIA driver 440.33.01 compared to 418.116.00 in DGX-2.
- For Lustre filesystem:
  -- with stripe count > 1, cuFileRead and cuFileWrite donot work with poll mode enabled for versions older than 2.12.5_ddn10.
  -- with 2.12.5_ddn10, any reads beyond EOF causes a BUG_ON inside nvidia-fs.
- RHEL8.3 does not have default udev rules for detecting RAID members, which disables GDS on RAID volumes. Please refer to the section “Adding udev Rules for RAID Volumes” in GDS 1.0.0 Troubleshooting guide.
- nfs-rdma module in MOFED 5.3-1.0.0.1 does not compile. Expected to be fixed in one of upcoming releases of MOFED 5.3
- max_direct_io_size_kb in cufile.json should be multiples of 64K.
- For IBM SpectrumScale, all the IO's that need to read beyond (16 * max_direct_io_size_kb) will be routed through bounce buffers.

XV. Known Limitations
========================================================

For Lustre, checksum is disabled in the read/write IO path.
For Weka, checksum is disabled in the read/write IO path.
There is no per GPU configuration for cache and BAR memory usage.
cuFile configuration is decided at application load time.
cuFile APIs are not supported with applications using the fork() system call.
There is no command or API to purge GDS internal caches without calling the cuFileDriverClose API.
MOFED 5.3 has been tested with following File systems - Ext4, DDN ExaScaler, WekaFS and IBM SpectrumScale. 
For IBM SpectrumScale, all the IO's that need to read beyond (16 * max_direct_io_size_kb) will be routed through bounce buffers.

IBM SpectrumScale Limitations and Known Issues
==================================

- IBM SpectrumScale does not support GDS mode on files less than 4096 bytes in length 
- IBM SpectrumScale does not support GDS mode on sparse files or files with pre-allocated storage (eg, fallocate(), gpfs_prealloc(), etc)
- IBM SpectrumScale does not support GDS mode on files that are encrypted or mmap-ed 
- IBM SpectrumScale does not support GDS mode on files that are compressed or marked for deferred compression (for more information on compression, 
  refer to www.ibm.com/docs/en/spectrum-scale/5.1.0?topic=reference-file-compression ) 
- IBM SpectrumScale in GDS mode does not support setting the mmchconfig option “disableDIO” to “true” (it must remain at the default value of “false”)

The cases listed above are handled in “compatibility mode”, providing correct operation but at a lower performance than GDS. In this mode, the NVIDIA GDS lib issues non-GDS Direct IO operation, and manually transfers data between the system memory buffer and the user application GPU buffer. 
 

- IBM SpectrumScale does not support GDS mode with data tiering, including transparent cloud tiering. The overhead of maintaining data 
  consistency in a tiered environment negates the performance benefit of GDS. 
- IBM SpectrumScale with GDS is not supported in asynchronous (“poll”) mode. The NVIDIA GDS lib ignores a poll 
  mode request for a file in a Spectrum Scale mount, converting the request to a synchronous GDS IO request.
- IBM SpectrumScale does not support GDS mode on files in snapshots or clones. If a GDS read is issued on a file in a snapshot or clone, -EIO is returned to the user application.
- IBM SpectrumScale in GDS mode has restriction where file sizes should be multiple of 4096 bytes. If a GDS read is issued on a file 
  with a size that is not a multiple of 4096 bytes, -EINVAL may be returned to the user application.
- With IBM SpectrumScale, running a GDS workload concurrent with a non-GDS workload on the same client is not recommended. Mixed workloads on a 
  client can eliminate the GDS performance benefit, and in rare cases, cause a kernel crash in GDS driver de-registration. 
 
XVI. License
========================================================

*** LICENSE AGREEMENT ***
By downloading and using this software you agree to fully comply with the terms and conditions of the CUDA EULA (End User License Agreement). The EULA is located
at EULA.txt. The EULA can also be found at http://docs.nvidia.com/cuda/eula/index.html. If you do not agree to the terms and conditions of the EULA, do not use the software.

XVII. Third Party Licenses
========================================================

1. Some of the libcufile_rdma.so/libcufile_rdma_static.a routines were written by or derived from copyrighted works of Mellanox Technologies and Licensee's use is subject to
OpenIB.org BSD License as follows:
 
License Text (https://spdx.org/licenses/Linux-OpenIB.html)
 
Copyright (c) 2012 Mellanox Technologies. -  All rights reserved.
 
This software is available to you under a choice of one of two
licenses.  You may choose to be licensed under the terms of the GNU
General Public License (GPL) Version 2, available from the file
COPYING in the main directory of this source tree, or the
OpenIB.org BSD license below:
 
     Redistribution and use in source and binary forms, with or
     without modification, are permitted provided that the following
     conditions are met:
 
      - Redistributions of source code must retain the above
        copyright notice, this list of conditions and the following
        disclaimer.
 
      - Redistributions in binary form must reproduce the above
        copyright notice, this list of conditions and the following
        disclaimer in the documentation and/or other materials
        provided with the distribution.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 
The khash functionality used in libcufile_rdma.so/libcufile_rdma_static.a is derived from Attractive Chaos and Licensee's use is subject to The MIT License
as follows:
 
Copyright Attractive Chaos - MIT License
 
The MIT License
 
Copyright (c) 2008, 2009, 2011 by Attractive Chaos <attractor@live.co.uk>
 
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:
 
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 
2. libcufile.so.1.0.0 and libcufile_static.a uses jsoncpp library's source code to be compiled into the libcufile.so.1.0.0, libcufile_static.a library. The license for the jsoncpp library is as follows.
 
 
 The JsonCpp library's source code, including accompanying documentation,
tests and demonstration applications, are licensed under the following
conditions...
 
The author (Baptiste Lepilleur) explicitly disclaims copyright in all
jurisdictions which recognize such a disclaimer. In such jurisdictions,
this software is released into the Public Domain.
 
In jurisdictions which do not recognize Public Domain property (e.g. Germany as of 2010), this software is Copyright (c) 2007-2010 by Baptiste Lepilleur, and is released under the terms of the MIT License (see below).
 
In jurisdictions which recognize Public Domain property, the user of this
software may choose to accept it either as 1) Public Domain, 2) under the
conditions of the MIT License (see below), or 3) under the terms of dual
Public Domain/MIT License conditions described here, as they choose.
 
The MIT License is about as close to Public Domain as a license can get, and is described in clear, concise terms at:
 
http://en.wikipedia.org/wiki/MIT_License
 
The full text of the MIT License follows:
 
========================================================================
Copyright (c) 2007-2010 Baptiste Lepilleur
 
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
========================================================================
(END LICENSE TEXT)
The MIT license is compatible with both the GPL and commercial
software, affording one all of the rights of Public Domain with the
minor nuisance of being required to keep the above copyright notice
and license text in the source code. Note also that by accepting the
Public Domain "license" you can re-license your copy using whatever
license you like.

Copyright 2009-2015 Samy Al Bahra.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.

3.

Copyright 2009-2015 Samy Al Bahra.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.

4. Some of the functionality in libcufile.so.1.0.0 uses uatomic.h from liburcu. The license text for that is as follows.

Copyright (c) 1991-1994 by Xerox Corporation.  All rights reserved.
Copyright (c) 1996-1999 by Silicon Graphics.  All rights reserved.
Copyright (c) 1999-2004 Hewlett-Packard Development Company, L.P.
Copyright (c) 2009      Mathieu Desnoyers
THIS MATERIAL IS PROVIDED AS IS, WITH ABSOLUTELY NO WARRANTY EXPRESSED
OR IMPLIED.  ANY USE IS AT YOUR OWN RISK.

Permission is hereby granted to use or copy this program
for any purpose,  provided the above notices are retained on all copies.
Permission to modify the code and to distribute modified code is granted,
provided the above notices are retained, and a notice that the code was
modified is included with the above copyright notice.

Code inspired from libuatomic_ops-1.2, inherited in part from the
Boehm-Demers-Weiser conservative garbage collector.

XVIII. Revision History
============================================================
please look at CHANGELOG for more details
[0.95.1] - 2021-05-11 - GDS open beta update 1 version
[0.95.0] - 2021-04-9  - GDS open beta
[0.9.0]  - 2020-11-02  - GDS open beta
[0.8.0]  - 2020-10-02  - GDS beta update 2 version
[0.7.1]  - 2020-06-04  - GDS beta update 1 version
[0.7.0]  - 2020-04-27  - GDS beta version
[0.5.0]  - 2019-08-29  - GDS alpha version
