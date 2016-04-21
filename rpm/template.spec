Name:           ros-indigo-iai-urdf-msgs
Version:        0.0.6
Release:        0%{?dist}
Summary:        ROS iai_urdf_msgs package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-message-runtime
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-message-generation

%description
Service definitions for manipulating the robot description.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Thu Apr 21 2016 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.0.6-0
- Autogenerated by Bloom

* Tue Dec 15 2015 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.0.5-3
- Autogenerated by Bloom

* Tue Dec 15 2015 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.0.5-2
- Autogenerated by Bloom

* Wed Nov 25 2015 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.0.5-1
- Autogenerated by Bloom

* Fri Apr 24 2015 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.0.5-0
- Autogenerated by Bloom

* Thu Mar 19 2015 Georg Bartels <georg.bartels@cs.uni-bremen.de> - 0.0.4-0
- Autogenerated by Bloom

