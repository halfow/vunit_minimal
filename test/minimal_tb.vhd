library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

library vunit_lib;
context vunit_lib.vunit_context;

entity tb_minimal is
  generic (
      runner_cfg : string
    );
end entity;

architecture tb of tb_minimal is
begin
  test_runner : process
  begin
    test_runner_setup(runner, runner_cfg);
    assert true; -- test goes here
    test_runner_cleanup(runner);
  end process;
end architecture;