my @perc;
my $fill = 'x';

enum Direction <DeadEnd Up Right Down Left>;

my $π = perctest(15);
.fmt("%-2s").say for @perc;
say "π± = 0.5, π = 15, π = $π\n";

my $trials = 5;
for 10, 30, 100, 300, 1000 -> $π {
    my $π = ( [+] perctest($π) xx $trials ) / $trials;
    say "π± = 0.5, trials = $trials, π = $π, π = $π";
}

sub infix:<deq> ( $a, $b ) { $a.defined && ($a eq $b) }

sub perctest ( $grid ) {
    generate $grid;
    my $block = 1;
    for ^$grid X ^$grid -> ($y, $x) {
        fill( [$x, $y], $block++ ) if @perc[$y; $x] eq $fill
    }
    ($block - 1) / $gridΒ²;
}

sub generate ( $grid ) {
    @perc = ();
    @perc.push: [ ( rand < .5 ?? '.' !! $fill ) xx $grid ] for ^$grid;
}

sub fill ( @cur, $block ) {
    @perc[@cur[1]; @cur[0]] = $block;
    my @stack;
    my $current = @cur;

    loop {
        if my $dir = direction( $current ) {
            @stack.push: $current;
            $current = move $dir, $current, $block
        }
        else {
            return unless @stack;
            $current = @stack.pop
        }
    }

    sub direction( [$x, $y] ) {
        ( Down  if @perc[$y + 1][$x] deq $fill ) ||
        ( Left  if @perc[$y][$x - 1] deq $fill ) ||
        ( Right if @perc[$y][$x + 1] deq $fill ) ||
        ( Up    if @perc[$y - 1][$x] deq $fill ) ||
        DeadEnd
    }

    sub move ( $dir, @cur, $block ) {
        my ( $x, $y ) = @cur;
        given $dir {
            when Up    { @perc[--$y; $x] = $block }
            when Down  { @perc[++$y; $x] = $block }
            when Left  { @perc[$y; --$x] = $block }
            when Right { @perc[$y; ++$x] = $block }
        }
        [$x, $y]
    }
}
