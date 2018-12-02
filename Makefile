CC					= ghc
SRC					= src
DIST				= dist
CORE				= Core
NAME				= alfred
BUILD				= $(DIST)/build/$(NAME)
BUILD-TEST	= $(BUILD)-test

all:
	make -s configure
	make -s build
	make -s clean

# FIXME: (Change this $(OS))
configure:
	[ -d $(BUILD) ] || mkdir -vp $(BUILD)

# FIXME: (Change this $(OS))
build:
	$(CC) -o $(BUILD)/$(NAME) `find $(SRC) -name '*.hs'`

# FIXME: (Change this $(OS))
clean:
	rm -rf $(DIST)/hpc
	rm -rf $(DIST)/test
	rm -rf $(BUILD)-tmp
	rm -rf $(DIST)/setup-config
	rm -rf $(BUILD)/$(NAME)-tmp
	rm -rf $(DIST)/build/$(CORE)
	rm -rf $(DIST)/build/autogen
	rm -rf $(DIST)/package.conf.inplace
	rm -rf $(BUILD-TEST)/$(NAME)-test-tmp
	find . -name "*.a" -type f -print0 | xargs -0 /bin/rm -f
	find . -name "*.o"  -type f -print0 | xargs -0 /bin/rm -f
	find . -name "*.hi" -type f -print0 | xargs -0 /bin/rm -f
	find . -name "*.so" -type f -print0 | xargs -0 /bin/rm -f
	find . -name "*.dyn_o" -type f -print0 | xargs -0 /bin/rm -f
	find . -name "*.dyn_hi" -type f -print0 | xargs -0 /bin/rm -f
