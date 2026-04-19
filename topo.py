from mininet.topo import Topo

class MyTopo(Topo):
    def build(self):
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')

        # hosts
        self.addLink(h1, s1)
        self.addLink(h2, s3)

        # main path
        self.addLink(s1, s2)
        self.addLink(s2, s3)

        # alternate path 🔥
        self.addLink(s1, s3)

# IMPORTANT LINE (this fixes your error)
topos = {'mytopo': (lambda: MyTopo())}
