import os

os.environ['LD_LIBRARY_PATH'] = '/usr/local/nvidia/lib:/usr/local/nvidia/lib64:/usr/local/cuda-9.0/lib64:/usr/local/cuda-9.0/lib64/libcudart.so.9.0'
c.Spawner.env.update('LD_LIBRARY_PATH')
c.Spawner.env_keep.append('LD_LIBRARY_PATH')

os.environ['ROS_PACKAGE_PATH'] = '/opt/ros/kinetic/share'
c.Spawner.env.update('ROS_PACKAGE_PATH')
c.Spawner.env_keep.append('ROS_PACKAGE_PATH')

os.environ['PYTHONPATH'] = '/opt/ros/kinetic/lib/python2.7/dist-packages'
c.Spawner.env.update('PYTHONPATH')
c.Spawner.env_keep.append('PYTHONPATH')

