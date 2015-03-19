Name:           ros-hydro-iai-kinematics-msgs
Version:        0.0.4
Release:        0%{?dist}
Summary:        ROS iai_kinematics_msgs package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-geometry-msgs
Requires:       ros-hydro-message-runtime
Requires:       ros-hydro-sensor-msgs
Requires:       ros-hydro-std-msgs
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-geometry-msgs
BuildRequires:  ros-hydro-message-generation
BuildRequires:  ros-hydro-sensor-msgs
BuildRequires:  ros-hydro-std-msgs

%description
Ensemble of messages to communicate/request kinematics-related issues.
NOTE/DISCLAIMER: A lot of these messages have been salvaged from now deprecated
packages arm_navigation_msgs and kinematics_msgs. We acknowledge original
authorship of these messages to all involved people (I, Georg, do not know them
by name).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Thu Mar 19 2015 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.0.4-0
- Autogenerated by Bloom

* Wed Dec 10 2014 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.0.3-1
- Autogenerated by Bloom

* Tue Oct 14 2014 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.0.3-0
- Autogenerated by Bloom

