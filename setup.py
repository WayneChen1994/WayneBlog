from setuptools import setup, find_packages

setup(
    name='WayneBlog',
    version='${version}',
    description='Blog System base on Django',
    author='Wayne.Chen',
    author_email='waynechen1994@163.com',
    url='http://www.wayne-chen.com',
    license='MIT',
    packages=find_packages('WayneBlog'),
    package_dir={'': 'WayneBlog'},
    package_data={'': [     # 方法一：打包数据文件
        'themes/*/*/*/*',   # 需要按目录层级匹配
    ]},
    # include_package_data=True,      # 方法二：配合MANIFEST.in文件
    install_requires=[
        'django~=1.11',
        'gunicorn==19.8.1',
        'supervisor==4.0.0dev0',
        'xadmin==0.6.1',
        'mysqlclient==1.3.12',
        'django-ckeditor==5.4.0',
        'django-rest-framework==0.1.0',
        'django-redis==4.8.0',
        'django-autocomplete-light==3.2.10',
        'mistune==0.8.3',
        'Pillow==4.3.0',
        'coreapi==2.3.3',
        'django-redis==4.8.0',
        'hiredis==0.2.0',
        # debug
        'django-debug-toolbar==1.9.1',
        'django-silk==2.0.0',
    ],
    extras_require={
        'ipython': ['ipython==6.2.1']
    },
    scripts=[
        'WayneBlog/manage.py',
    ],
    entry_points={
        'console_scripts': [
            'WayneBlog_manage = manage:main',
        ]
    },
    classifiers=[
        # 软件成熟度如何？一般有下面几种选项
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # 指明项目的受众
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        # 选择项目的许可证（License）
        'License :: OSI Approved :: MIT License',

        # 指定项目需要使用的Python版本
        'Programming Language :: Python :: 3.6',
    ],
)
