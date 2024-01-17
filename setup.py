from setuptools import setup
import setup_translate

pkg = 'SystemPlugins.QuadPiP'
setup(name='enigma2-plugin-systemplugins-quadpip',
	version='1.20',
	description='QuadPiP plugin for GigaBlue & VU+ UHD receivers',
	packages=[pkg],
	package_dir={pkg: 'plugin'},
	package_data={pkg: ['*.xml', 'locale/*/LC_MESSAGES/*.mo']},
	cmdclass=setup_translate.cmdclass, # for translation
	)
